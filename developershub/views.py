from django.shortcuts import render


def index(requets):
    context = {
        "ready": True
    }
    return render(requets, 'developershub/index.html', context)
