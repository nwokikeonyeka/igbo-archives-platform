from django.shortcuts import render

def coming_soon(request):
    """Academy coming soon page with details about future features."""
    return render(request, 'academy/coming_soon.html')
