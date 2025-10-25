from django.shortcuts import render

def insight_list(request):
    return render(request, 'insights/list.html')
