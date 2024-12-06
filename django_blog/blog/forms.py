from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from taggit.forms import TagWidget  # If you're using django-taggit for tags

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  # TagWidget is used to display tags input
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in form fields

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Optionally, you can create a widget for other custom uses:
class CustomTagWidget(forms.TextInput):
    # Define the custom widget behavior if needed
    pass
