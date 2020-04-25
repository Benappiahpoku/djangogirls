from django import forms

from . models import Post

# create you class

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'text',)