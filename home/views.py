from django.shortcuts import render
from home.models import Page


def page_index(request):
    home = Page.objects.all()
    context = {
        'home': home
    }
    return render(request, 'page_index.html', context)

def page_detail(request, pk):
    page = Page.objects.get(pk=pk)
    context = {
        "page": page
    }
    return render(request, 'page_detail.html', context)