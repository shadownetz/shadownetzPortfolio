from django.shortcuts import render


def index(request):
    context = {
        'ready': True
    }
    return render(request, 'blog/index.html', context)
