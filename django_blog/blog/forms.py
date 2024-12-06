from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from taggit.forms import TagWidget  # For handling tags if using django-taggit

# Post creation and update form with a custom widget for tags
class PostForm(forms.ModelForm):
    # Define the tags field with TagWidget if using django-taggit
    tags = forms.CharField(
        widget=TagWidget(),  # Uses TagWidget to allow tag input
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form fields

# Comment form doesn't require a custom widget but could include one if needed
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Optional: Define a custom widget for any form field
class CustomTagWidget(forms.TextInput):
    template_name = 'custom_widget_template.html'  # Specify the template for the widget

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({'class': 'custom-class'})  # Add custom classes or attributes
        super().__init__(attrs)

# Another example: using a custom widget for another form field
class CustomContentWidget(forms.Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({'class': 'custom-textarea-class'})
        super().__init__(attrs)
