from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import InsightPost, EditSuggestion
from django.core.paginator import Paginator
from django.utils.text import slugify

def insight_list(request):
    insights = InsightPost.objects.filter(is_published=True, is_approved=True)
    
    search = request.GET.get('search')
    if search:
        insights = insights.filter(title__icontains=search)
    
    tag = request.GET.get('tag')
    if tag:
        insights = insights.filter(tags__name=tag)
    
    sort = request.GET.get('sort', '-created_at')
    insights = insights.order_by(sort)
    
    paginator = Paginator(insights, 12)
    page = request.GET.get('page')
    insights = paginator.get_page(page)
    
    if request.htmx:
        return render(request, 'insights/partials/insight_grid.html', {'insights': insights})
    
    return render(request, 'insights/list.html', {'insights': insights})

def insight_detail(request, slug):
    insight = get_object_or_404(InsightPost, slug=slug, is_published=True)
    return render(request, 'insights/detail.html', {'insight': insight})

@login_required
def insight_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt')
        
        insight = InsightPost.objects.create(
            title=title,
            slug=slugify(title),
            content=content,
            excerpt=excerpt,
            author=request.user,
            featured_image=request.FILES.get('featured_image'),
            alt_text=request.POST.get('alt_text', ''),
            is_published=request.POST.get('is_published') == 'on'
        )
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                insight.tags.add(tag.strip())
        
        return redirect('insights:detail', slug=insight.slug)
    
    return render(request, 'insights/create.html')

@login_required
def suggest_edit(request, slug):
    insight = get_object_or_404(InsightPost, slug=slug)
    if request.method == 'POST':
        suggestion_text = request.POST.get('suggestion')
        EditSuggestion.objects.create(
            post=insight,
            suggested_by=request.user,
            suggestion_text=suggestion_text
        )
        return redirect('insights:detail', slug=slug)
    return render(request, 'insights/suggest_edit.html', {'insight': insight})
