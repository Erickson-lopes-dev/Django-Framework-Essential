from django.contrib import messages
from django.shortcuts import render

from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    # pode passar paremetros vazios ou com formulario
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f'Post: {request.POST}')
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f'{nome} {email}, {assunto} {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso')

            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar o e-mail")
    context = {
        'form': form,
    }

    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
