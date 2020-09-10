from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Progamação web com python e django'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
