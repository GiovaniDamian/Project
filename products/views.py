from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Product, ProductSala, ProductQuarto, ProductLimpeza, ProductEletronico, ProductCozinha, ProductAcampamento, ProductBanheiro, ProductCapacetes

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponsePermanentRedirect('https://docs.google.com/forms/d/e/1FAIpQLSchsSK_vhamTs9HzRZRI8zlEELmddZQQ-1LXs4DOOSEc8O-Mg/viewform?usp=sf_link',)


def sala(request):
    sala = ProductSala.objects.all()
    return render(request, 'sala.html',
                  {'sala': sala})


def eletronicos(request):
    eletronico = ProductEletronico.objects.all()
    return render(request, 'eletronicos.html',
                  {'eletronico': eletronico})


def limpeza(request):
    limpeza = ProductLimpeza.objects.all()
    return render(request, 'limpeza.html',
                  {'limpeza': limpeza})


def quarto(request):
    quarto = ProductQuarto.objects.all()
    return render(request, 'quarto.html',
                  {'quarto': quarto})


def banheiro(request):
    banheiro = ProductBanheiro.objects.all()
    return render(request, 'banheiro.html',
                  {'banheiro': banheiro})


def capacetes(request):
    capacete = ProductCapacetes.objects.all()
    return render(request, 'capacetes.html',
                  {'capacete': capacete})


def acamp(request):
    acamp = ProductAcampamento.objects.all()
    return render(request, 'acampamento.html',
                  {'acamp': acamp})


def cozinha(request):
    cozinha = ProductCozinha.objects.all()
    return render(request, 'cozinha.html',
                  {'cozinha': cozinha})