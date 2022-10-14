from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['movie', 'title', 'content', 'grade']

class MovieArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'grade']