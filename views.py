from django.http import HttpResponseRedirect

from forms import FormRegistro, FormContato
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail


def index(request):
    return render_to_response(
                              'index.html',
                              locals(),
                              context_instance=RequestContext(request),)


def contato(request): 
    if request.method == "POST":
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            mostrar = 'Contato Enviado'
        else:
            form = FormContato()
            
    return render_to_response(
                              'contato.html',
                              locals(),
                              context_instance=RequestContext(request),)


def registrar(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormRegistro()

    return render_to_response(
        'registrar.html',
        locals(),
        context_instance=RequestContext(request),
        )
