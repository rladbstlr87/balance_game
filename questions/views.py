from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
import random

# Create your views here.

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:index')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    comments = article.comment_set.all()
    count_A = article.comment_set.filter(AB='A').count()
    count_B = article.comment_set.filter(AB='B').count()

    context = {
        'article': article,
        'form': form,
        'comments': comments,
        'count_A': count_A,
        'count_B': count_B,
    }

    return render(request, 'detail.html', context)

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('questions:detail', id=article_id)

    else:
        return redirect('questions:index')
            

def random_page(request):
    articles = Article.objects.all()
    article = random.choice(articles)
    return redirect('questions:detail', id=article.id)

from .forms import CommentForm