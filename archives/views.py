from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Archive, Category
from django.core.paginator import Paginator

def archive_list(request):
    archives = Archive.objects.all()
    
    category = request.GET.get('category')
    if category:
        archives = archives.filter(category__slug=category)
    
    search = request.GET.get('search')
    if search:
        archives = archives.filter(title__icontains=search)
    
    archive_type = request.GET.get('type')
    if archive_type:
        archives = archives.filter(archive_type=archive_type)
    
    sort = request.GET.get('sort', '-created_at')
    archives = archives.order_by(sort)
    
    paginator = Paginator(archives, 12)
    page = request.GET.get('page')
    archives = paginator.get_page(page)
    
    categories = Category.objects.all()
    featured = Archive.objects.filter(is_featured=True)[:5]
    
    context = {
        'archives': archives,
        'categories': categories,
        'featured': featured
    }
    
    if request.htmx:
        return render(request, 'archives/partials/archive_grid.html', context)
    
    return render(request, 'archives/list.html', context)

def archive_detail(request, pk):
    archive = get_object_or_404(Archive, pk=pk)
    return render(request, 'archives/detail.html', {'archive': archive})

@login_required
def archive_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        archive_type = request.POST.get('archive_type')
        category_id = request.POST.get('category')
        alt_text = request.POST.get('alt_text')
        
        archive = Archive.objects.create(
            title=title,
            description=description,
            archive_type=archive_type,
            category_id=category_id,
            image=request.FILES.get('image'),
            alt_text=alt_text,
            uploaded_by=request.user
        )
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                archive.tags.add(tag.strip())
        
        return redirect('archives:detail', pk=archive.pk)
    
    categories = Category.objects.all()
    return render(request, 'archives/create.html', {'categories': categories})
