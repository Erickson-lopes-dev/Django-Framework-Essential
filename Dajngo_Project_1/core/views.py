from django.shortcuts import render


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

    context = {
        'curso': 'Progamação web com python e django',
        'teste': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
