from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'photo', 'publicity', 'language', 'time_life']
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'paste-textarea',
                'placeholder': 'Вставьте ваш текст здесь...',
                'cols': '40',
                'rows': '8',
            }),
            'language': forms.Select(attrs={'class': 'language-select'})
        }
