from django.db import models
from datetime import datetime
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body_blurb = models.TextField(max_length=200)
    body_text = MarkdownxField()
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return self.slug

    @property
    def formatted_markdown(self):
        return markdownify(self.body_text)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Email(models.Model):
    email_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    email_body = models.TextField(max_length=1000)
    email_subject = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.email_address

    class Meta:
        verbose_name_plural = "Emails"


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    comment = models.TextField(max_length=1000)
    pub_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.post.title, self.name, self.pub_date)

    class Meta:
        verbose_name_plural = "Comments"
