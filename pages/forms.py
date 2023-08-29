from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body','author']


class DeletePostForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput(),  # Hide the checkbox
        initial=True,
    )

        
    # You can add additional form field customization here if needed
