from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article

def article_list(request):
    """لیست مقالات"""
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    
    # فیلتر بر اساس دسته‌بندی
    category = request.GET.get('category')
    if category:
        articles = articles.filter(category=category)
    
    # جستجو
    search = request.GET.get('search')
    if search:
        articles = articles.filter(title__icontains=search) | articles.filter(content__icontains=search)
    
    # صفحه‌بندی
    paginator = Paginator(articles, 12)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    return render(request, 'magazine/list.html', {
        'articles': articles,
        'categories': Article.CATEGORY_CHOICES
    })

def article_detail(request, slug):
    """جزئیات مقاله"""
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'magazine/detail.html', {'article': article})
