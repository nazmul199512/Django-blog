from django import forms
from .models import  Blog,Comment,Like

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )


