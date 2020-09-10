from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=6)
    estoque = models.IntegerField('Quantidade em Estoque')
    created_at = models.DateTimeField(auto_now_add=True)


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
