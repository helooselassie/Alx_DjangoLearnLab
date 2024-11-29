# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article

@login_required
@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@login_required
@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content, author=request.user)
        return render(request, 'article_detail.html', {'article': article})
    return render(request, 'article_form.html')

@login_required
@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return render(request, 'article_detail.html', {'article': article})
    return render(request, 'article_form.html', {'article': article})

@login_required
@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        return render(request, 'article_list.html')
    return render(request, 'article_confirm_delete.html', {'article': article})
