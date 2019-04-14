from django.shortcuts import render, get_object_or_404
from .models import Article
from django import forms


# Create your views here.
# def index(request):
#     return HttpResponse('Hi there!')


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail.html', {'article': article})


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
