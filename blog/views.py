from django.shortcuts import render


def index(request):
    context = {
        'ready': False
    }
    return render(request, 'blog/index.html', context)
