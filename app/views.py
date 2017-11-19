
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from app.serializers import comment_serializer
from app.forms import ContactForm, CommentForm
from .models import Post, Email, Category, Comment


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    post_list = Post.objects.all().order_by('-pub_date')
    categories = Category.objects.all().order_by('name')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts, 'categories': categories})


def blog_filter(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-pub_date')
    categories = Category.objects.all().order_by('name')
    return render(request, 'blog.html', {'posts': posts, 'categories': categories})


def portfolio(request):
    return render(request, 'portfolio.html')


def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.all().filter(post__slug=slug)
    comment_form = CommentForm
    return render(request, 'blog_post.html', {'post': post, "comment_form": comment_form, "comments": comments})


def contact_submit(request):
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(data=request.POST)
        if request.is_ajax():
            if form.is_valid():
                email_address = request.POST['email_address']
                email_body = request.POST['email_body']
                email_name = request.POST['email_name']
                email_subject = request.POST['email_subject']
                to_email = settings.EMAIL_HOST_USER
                email_subject_concat = "Email @ Personal Site From: " + email_name + " About: " + email_subject
                try:
                    send_mail(
                        email_subject_concat,
                        email_body,
                        email_address,
                        [to_email],
                        fail_silently=False,
                    )
                    email_model = Email(email_subject=email_subject, email_name=email_name,
                                        email_address=email_address,
                                        email_body=email_body)
                    email_model.save(force_insert=True)
                    return JsonResponse({"status": 'true'})
                except BadHeaderError:
                    return HttpResponse('Invalid Header Found')
            else:
                errors = dict([(k, [e for e in v]) for k, v in form.errors.items()])
                return JsonResponse(errors)
        else:
            print("No Post?")

        return render(request, 'contact.html')


def comment_submit(request, slug):
    Post.objects.filter(slug=slug).exists()
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm
    if request.method == 'POST':
        form = comment_form(data=request.POST)
        if request.is_ajax():
            if form.is_valid():
                name = request.POST['name']
                email = request.POST['email']
                comment = request.POST['comment']
                try:
                    comment_model = Comment(post=post, name=name, email=email, comment=comment)
                    comment_model.save(force_insert=True)
                    comments = Comment.objects.all().filter(post__slug=slug)
                    serialized_comments = comment_serializer(comments)
                    return JsonResponse({"status": 'true', "comments": serialized_comments})
                except BadHeaderError:
                    return HttpResponse('Invalid Header Found')
            else:
                errors = dict([(k, [e for e in v]) for k, v in form.errors.items()])
                return JsonResponse(errors)
        else:
            print("No Post?")

        return render(request, 'blog.html')


def error_handler_404(request):
    render(request, '404.html')


def error_handler_500(request):
    render(request, '500.html')

