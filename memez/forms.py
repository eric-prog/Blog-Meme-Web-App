from django import forms
from . import models


class CreateMeme(forms.ModelForm):
    class Meta:
        model = models.Meme
        fields = ['title', 'body', 'slug', 'thumb']