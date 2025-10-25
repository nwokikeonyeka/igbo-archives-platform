from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BookReview
from django.core.paginator import Paginator
from django.utils.text import slugify

def book_list(request):
    reviews = BookReview.objects.filter(is_published=True)
    
    search = request.GET.get('search')
    if search:
        reviews = reviews.filter(book_title__icontains=search) | reviews.filter(review_title__icontains=search)
    
    tag = request.GET.get('tag')
    if tag:
        reviews = reviews.filter(tags__name=tag)
    
    rating = request.GET.get('rating')
    if rating:
        reviews = reviews.filter(rating=rating)
    
    sort = request.GET.get('sort', '-created_at')
    reviews = reviews.order_by(sort)
    
    paginator = Paginator(reviews, 12)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    
    if request.htmx:
        return render(request, 'books/partials/book_grid.html', {'reviews': reviews})
    
    return render(request, 'books/list.html', {'reviews': reviews})

def book_detail(request, slug):
    review = get_object_or_404(BookReview, slug=slug, is_published=True)
    return render(request, 'books/detail.html', {'review': review})

@login_required
def book_create(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        review_title = request.POST.get('review_title')
        
        # Generate unique slug
        base_slug = slugify(review_title)
        slug = base_slug
        counter = 1
        while BookReview.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        review = BookReview.objects.create(
            book_title=book_title,
            author=request.POST.get('author'),
            isbn=request.POST.get('isbn', ''),
            review_title=review_title,
            slug=slug,
            content=request.POST.get('content'),
            rating=int(request.POST.get('rating')),
            reviewer=request.user,
            cover_image=request.FILES.get('cover_image'),
            is_published=request.POST.get('is_published') == 'on'
        )
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                review.tags.add(tag.strip())
        
        messages.success(request, 'Your book review has been created successfully!')
        return redirect('books:detail', slug=review.slug)
    
    return render(request, 'books/create.html')

@login_required
def book_edit(request, slug):
    review = get_object_or_404(BookReview, slug=slug, reviewer=request.user)
    
    if request.method == 'POST':
        review.book_title = request.POST.get('book_title')
        review.author = request.POST.get('author')
        review.isbn = request.POST.get('isbn', '')
        review.review_title = request.POST.get('review_title')
        review.content = request.POST.get('content')
        review.rating = int(request.POST.get('rating'))
        review.is_published = request.POST.get('is_published') == 'on'
        
        if request.FILES.get('cover_image'):
            review.cover_image = request.FILES.get('cover_image')
        
        # Clear existing tags and add new ones
        review.tags.clear()
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                review.tags.add(tag.strip())
        
        review.save()
        messages.success(request, 'Your book review has been updated successfully!')
        return redirect('books:detail', slug=review.slug)
    
    return render(request, 'books/edit.html', {'review': review})
