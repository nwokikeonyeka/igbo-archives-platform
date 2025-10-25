from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BookReview
from django.core.paginator import Paginator
from django.utils.text import slugify

def book_list(request):
    books = BookReview.objects.filter(is_published=True)
    
    search = request.GET.get('search')
    if search:
        books = books.filter(book_title__icontains=search)
    
    rating = request.GET.get('rating')
    if rating:
        books = books.filter(rating=rating)
    
    sort = request.GET.get('sort', '-created_at')
    books = books.order_by(sort)
    
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    
    if request.htmx:
        return render(request, 'books/partials/book_grid.html', {'books': books})
    
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(BookReview, slug=slug, is_published=True)
    return render(request, 'books/detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        book = BookReview.objects.create(
            book_title=request.POST.get('book_title'),
            author=request.POST.get('author'),
            isbn=request.POST.get('isbn', ''),
            review_title=request.POST.get('review_title'),
            slug=slugify(request.POST.get('review_title')),
            content=request.POST.get('content'),
            rating=int(request.POST.get('rating')),
            cover_image=request.FILES.get('cover_image'),
            reviewer=request.user,
            is_published=request.POST.get('is_published') == 'on'
        )
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            if tag.strip():
                book.tags.add(tag.strip())
        
        return redirect('books:detail', slug=book.slug)
    
    return render(request, 'books/create.html')
