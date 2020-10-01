from django.db.models import fields
from .models import Comment
from django import forms

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')