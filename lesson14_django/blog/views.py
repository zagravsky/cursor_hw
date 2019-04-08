from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse('Hi there!')


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

