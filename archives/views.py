from django.shortcuts import render

def archive_list(request):
    return render(request, 'archives/list.html')
