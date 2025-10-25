from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        date_created = request.POST.get('date_created') or None
        
        archive = Archive.objects.create(
            title=title,
            description=description,
            archive_type=archive_type,
            category_id=category_id if category_id else None,
            image=request.FILES.get('image'),
            alt_text=alt_text,
            date_created=date_created,
            uploaded_by=request.user
        )
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                archive.tags.add(tag.strip())
        
        messages.success(request, 'Archive uploaded successfully!')
        return redirect('archives:detail', pk=archive.pk)
    
    categories = Category.objects.all()
    return render(request, 'archives/create.html', {'categories': categories})

@login_required
def archive_edit(request, pk):
    archive = get_object_or_404(Archive, pk=pk, uploaded_by=request.user)
    
    if request.method == 'POST':
        archive.title = request.POST.get('title')
        archive.description = request.POST.get('description')
        archive.archive_type = request.POST.get('archive_type')
        archive.category_id = request.POST.get('category') if request.POST.get('category') else None
        archive.alt_text = request.POST.get('alt_text')
        archive.date_created = request.POST.get('date_created') or None
        
        if request.FILES.get('image'):
            archive.image = request.FILES.get('image')
        
        # Clear existing tags and add new ones
        archive.tags.clear()
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                archive.tags.add(tag.strip())
        
        archive.save()
        messages.success(request, 'Archive updated successfully!')
        return redirect('archives:detail', pk=archive.pk)
    
    categories = Category.objects.all()
    return render(request, 'archives/edit.html', {'archive': archive, 'categories': categories})
