from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    # pode passar paremetros vazios ou com formulario
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f'Post: {request.POST}')
        if form.is_valid():

            form.send_email()

            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']
            #
            # print(f'{nome} {email}, {assunto} {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso')

            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar o e-mail")
    context = {
        'form': form,
    }

    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != "AnonymousUser":
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Produto salvo com sucesso')

                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm

        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')

