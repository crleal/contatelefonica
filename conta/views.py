# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.forms import ModelForm



from conta.models import Conta
from conta.models import ContaDetalhe
from conta.models import Loja, Nextel, Ramal, Setorramal


#Classes ModelForm
class ContaModelForm(ModelForm):
    class Meta:
        model = Conta


class ContaDetalheModelForm(ModelForm):
    class Meta:
        model = ContaDetalhe
#Classes ModelForm


# Inicio CRUD Conta
def index_conta(request):
    Contas = Conta.objects.all().order_by('num_conta')
    return render_to_response('conta/index.html',
                   locals(), context_instance=RequestContext(request))


def nova_conta(request):
    if request.POST:
        form = ContaModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/conta/')
        else:
            return HttpResponse(form.errors)
    else:
        form = ContaModelForm()
    return render_to_response('conta/incluir.html',  locals(),
                         context_instance=RequestContext(request))


#def apagar_municipio(request, codigo):
#    c = get_object_or_404(Municipio, pk=codigo)
#    nome = c.nome
#    c.delete()
#    f = ContatosModelForm()
#    c = Contatos.objects.all()
#    return render_to_response('contatos.html',
#                     {'form':f.as_table(), 'nome':nome, 'c':c})


def alterar_conta(request, id):
    conta = Conta.objects.get(pk=id)
    if request.method == 'POST':
        form = ContaModelForm(request.POST, instance=conta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/conta/')
    else:
        form = ContaModelForm(instance=conta)

    return render_to_response('conta/alterar.html', locals(),
                           context_instance=RequestContext(request))


#Fim CRUD Conta

# Inicio CRUD ContaDetalhe
def index_contadetalhe(request):
    ContaDetalhes = ContaDetalhe.objects.all().order_by('num_conta')    
    return render_to_response('contadetalhe/index.html',
                   locals(), context_instance=RequestContext(request))


def alterar_contadetalhe(request, id):
    contadetalhe = ContaDetalhe.objects.get(pk=id)
    if request.method == 'POST':
        form = ContaDetalheModelForm(request.POST, instance=contadetalhe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contadetalhe/')
    else:
        form = ContaDetalheModelForm(instance=contadetalhe)

    return render_to_response('contadetalhe/alterar.html', locals(),
                           context_instance=RequestContext(request))


#Fim CRUD ContaDetalhe

#
#class filtra_contadetalhe(self) :
#    ContaDetalhes = ContaDetalhe.objects.filter(tel_origem__contains=self.tel).order_by('num_conta')
#       render_to_response('contadetalhe/index.html',
#                   locals(), context_instance=RequestContext(request))

#    ContaDetalhes = ContaDetalhe.objects.filter(tel_origem__contains=tel).order_by('num_conta')
#    return render_to_response('conta/index_contadetalhe.html',
#                   locals(), context_instance=RequestContext(request))


def consulta_ramal(request):
    loja = Loja.objects.all()
    Celulares = Nextel.objects.filter(consulta=1).order_by("nome")
    Ramals = Ramal.objects.filter(consulta=1).order_by("nome") 
    setorramal = Setorramal.objects.all() 

    idloja = 0
    idsetor = 0 
    
    return render_to_response('consulta_ramal.html',
                   locals(), context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------------------   
def consulta_ramal_procura(request, idloja, idsetor):
    Ramals = Ramal.objects.filter(consulta=1).order_by("nome") 
    Celulares = Nextel.objects.filter(consulta=1).order_by("nome")
    if idloja != "0":
        Ramals = Ramals.filter(lojaid=idloja)
        Celulares = Celulares.filter(lojaid=idloja)
    if idsetor != "0":
        Ramals = Ramals.filter(setorramalid=idsetor)
        Celulares = Celulares.filter(setorramalid=idsetor)

    idloja = idloja
    idsetor = idsetor 
  
    loja = Loja.objects.all() 
    setorramal = Setorramal.objects.all() 

    return render_to_response('consulta_ramal.html',
                   locals(), context_instance=RequestContext(request))
