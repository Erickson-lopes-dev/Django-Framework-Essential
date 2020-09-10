from django.shortcuts import render

from .models import Produto


def index(request):
    # retorna o objeto da request
    print('Objeto: ' + str(request))

    # retorna o método requisitado
    print('Método: ' + request.method)

    # retorna o usuário logado
    print('Usuário: ' + str(request.user))

    if request.user == "AnonymousUser":
        teste = 'Logado'
    else:
        teste = 'Usuario não logado'

    # print(dir(request.user))

    produtos = Produto.objects.all()

    context = {
        'curso': 'Progamação web com python e django',
        'teste': teste,
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    context = Produto.objects.get(id=id)

    return render(request, 'produto.html', {'produto':context})