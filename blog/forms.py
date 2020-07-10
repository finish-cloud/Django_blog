# myproject/forms.py
from django.forms import ModelForm, TextInput, Textarea

from blog.models import Comment, Reply
from django.core.exceptions import ValidationError
from .models import Post
from django import forms


def validate_confirm(value):
    if value != '確認':
        raise ValidationError(
            "漢字で正しく入力してください。",
            params={'value': value},
        )


class PostForm(forms.ModelForm):
    """投稿フォーム"""
    confirm = forms.CharField(
        label="上記の内容でよろしければ、最後に「確認」と入力して送信ボタンを押してください",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[validate_confirm],
    )

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '返信内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }
