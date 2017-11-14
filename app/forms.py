from django.forms import ModelForm
from app.models import Email, Comment


class ContactForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email_name', 'email_body', 'email_address', 'email_subject']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']