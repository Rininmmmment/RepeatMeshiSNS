from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# ホーム画面
def index(request):
    context = {
        'articles': Article.objects.all().order_by('-id'),
    }
    return render(request, 'main/index.html', context)

# タイムライン
def timeline(request):
    context = {
        'articles': Article.objects.all().order_by('-id'),
    }
    return render(request, 'main/timeline.html', context)

# 投稿画面
class create(CreateView):
    template_name = "main/create.html"
    form_class = ArticleForm
    success_url = "/main/"
    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs["user"] = self.request.user
        return kwgs

# 詳細画面
def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article,
    }
    return render(request, 'main/detail.html', context)

# マイページ画面
def mypage(request):
    context = {
        'articles': Article.objects.all().order_by('-id'),
    }
    return render(request, 'main/mypage.html', context)

# 投稿削除
def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    if article.user == request.user:
        article.delete()

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return redirect('main:index')