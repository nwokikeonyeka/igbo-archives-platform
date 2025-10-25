from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InsightPost, EditSuggestion
from archives.models import Archive
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
    archive_id = request.GET.get('archive_id')
    initial_title = ''
    initial_content = ''
    initial_excerpt = ''
    archive_title = ''
    
    if archive_id:
        try:
            archive = Archive.objects.get(id=archive_id)
            archive_title = archive.title
            initial_title = f"Insights on {archive.title}"
            initial_content = f"<p>Related to <a href='/archives/{archive.id}/'>'{archive.title}'</a></p><p>{archive.description}</p>"
            initial_excerpt = f"A reflection on {archive.title}"
        except Archive.DoesNotExist:
            pass
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt', '')
        
        # Generate unique slug
        base_slug = slugify(title)
        slug = base_slug
        counter = 1
        while InsightPost.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        insight = InsightPost.objects.create(
            title=title,
            slug=slug,
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
        
        messages.success(request, 'Your insight has been created successfully!')
        return redirect('insights:detail', slug=insight.slug)
    
    context = {
        'archive_title': archive_title,
        'initial_title': initial_title,
        'initial_content': initial_content,
        'initial_excerpt': initial_excerpt,
    }
    return render(request, 'insights/create.html', context)

@login_required
def insight_edit(request, slug):
    insight = get_object_or_404(InsightPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        insight.title = request.POST.get('title')
        insight.excerpt = request.POST.get('excerpt', '')
        insight.content = request.POST.get('content')
        insight.alt_text = request.POST.get('alt_text', '')
        insight.is_published = request.POST.get('is_published') == 'on'
        
        if request.FILES.get('featured_image'):
            insight.featured_image = request.FILES.get('featured_image')
        
        # Clear existing tags and add new ones
        insight.tags.clear()
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                insight.tags.add(tag.strip())
        
        insight.save()
        messages.success(request, 'Your insight has been updated successfully!')
        return redirect('insights:detail', slug=insight.slug)
    
    return render(request, 'insights/edit.html', {'insight': insight})

@login_required
def suggest_edit(request, slug):
    insight = get_object_or_404(InsightPost, slug=slug)
    if request.method == 'POST':
        suggestion_text = request.POST.get('suggestion')
        EditSuggestion.objects.create(
            post=insight,
            suggested_by=request.user if request.user.is_authenticated else None,
            suggestion_text=suggestion_text
        )
        messages.success(request, 'Thank you! Your edit suggestion has been sent to the author.')
        return redirect('insights:detail', slug=slug)
    return render(request, 'insights/suggest_edit.html', {'insight': insight})
