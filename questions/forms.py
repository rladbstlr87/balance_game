from django.forms import ModelForm
from .models import Article, Comment
from django import forms

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'

class CommentForm(ModelForm):
    
    class Meta():
        model = Comment
        exclude = ('article', )
        # AB = forms.ChoiceField()
        # choices = [(1, 'A'), (2, 'B')]
        widgets={
            'AB': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요.'})
            }
            