# LibraryProject/bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    # Example fields
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        # Custom validation
        data = self.cleaned_data['message']
        if len(data) < 10:
            raise forms.ValidationError("Message is too short!")
        return data
