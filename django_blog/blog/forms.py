from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # Import TagWidget if using django-taggit for tags

# Post creation and update form with custom widgets
class PostForm(forms.ModelForm):
    # Custom widget for the 'tags' field, if using django-taggit
    tags = forms.CharField(
        widget=TagWidget(),  # Uses the TagWidget for tag input
        required=False
    )
    
    # You can also customize other fields if necessary
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))  # Custom textarea widget

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form fields

# Comment form with no widget customization needed (but can be customized if needed)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Optionally define a custom widget if needed for other fields
class CustomTextWidget(forms.Textarea):
    def __init__(self, attrs=None):
        # You can add custom attributes for the widget here
        if attrs is None:
            attrs = {}
        attrs.update({'class': 'custom-text-widget', 'placeholder': 'Enter text here...'})
        super().__init__(attrs)

# Using the CustomTextWidget in a form
class CustomPostForm(forms.ModelForm):
    content = forms.CharField(widget=CustomTextWidget(attrs={'rows': 5, 'cols': 60}))  # Apply custom widget

    class Meta:
        model = Post
        fields = ['title', 'content']
