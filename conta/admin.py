from django.contrib import admin
#from django.contrib.admin.options import ModelAdmin
from models import Conta, ContaDetalhe, ContaServico, Numero, Departamento, Filial, Loja, Nextel, Ramal, Setorramal
from utils.utils import *

class FilialAdmin(admin.ModelAdmin):
    list_display = ('codfilial', 'nome',)
    search_fields = ('nome', )
    list_per_page = 40
    ordering = ('nome',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', )
    list_per_page = 40
    ordering = ('nome',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)


class ContaAdmin(admin.ModelAdmin):
    list_display = ('num_conta', 'codfilial','dt_emissao', 'dt_inicio', 'dt_final', 'dt_vencimento', 'vl_nota',  'vlr_ajuste')
    list_filter = ('codfilial',)
    #search_fields = ('dept_name',)
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)


class ContaDetalheAdmin(admin.ModelAdmin):
    list_display = ('num_conta', 'nun_seq', 'numero_tel', 'tipo', 'dt_lig', 'origem', 'tel_origem', 
                    'destino', 'tel_destino', 'duracao', 'horario', 'servico', 'vlr_lig')
    list_filter = ('num_conta', 'servico', 'horario', 'tipo',)
    search_fields = ('numero_tel__numero_tel', 'tel_origem', 'tel_destino', )
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)

class NumerosAdmin(admin.ModelAdmin):
    list_display = ('numero_tel',)
    search_fields = ('numero_tel', )
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('lojaid','nomeloja', 'tel', 'email', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'ativo', )
    search_fields = ('loja', )
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)

class NextelAdmin(admin.ModelAdmin):
    list_display = ('celular', 'lojaid', 'setorramalid', 'nome', 'ramal', 'id', 'consulta')
    list_filter = ('lojaid', 'consulta', 'setorramalid', )
    search_fields = ('celular', 'lojaid__nomeloja', 'setorramalid__setor', 'nome', 'ramal', 'id')
    list_per_page = 40
    actions = None

    def construct_change_message(self, request, form, formsets):
        return troca_message(self, request, form, formsets)


class RamalAdmin(admin.ModelAdmin):
    list_display = ('ramal', 'setorramalid', 'lojaid', 'nome', 'consulta')
    search_fields = ('ramal', 'setorramalid__setor', 'lojaid__nomeloja', 'nome',)
    list_filter = ('lojaid', 'consulta', 'setorramalid', )
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)

class SetorramalAdmin(admin.ModelAdmin):
    list_display = ('setor',)
    search_fields = ('setor', )
    list_per_page = 40
    #ordering = ('dept_name',)
    actions = None
    #form = DotpProjectsForm 
    #change_form_template = 'projeto/change_form.html'

    def construct_change_message(self, request, form, formsets):
        """
        Construct a change message from a changed object.
        """
        return troca_message(self, request, form, formsets)




admin.site.register(Numero, NumerosAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Conta, ContaAdmin)
admin.site.register(ContaDetalhe, ContaDetalheAdmin)

admin.site.register(Loja, LojaAdmin)
admin.site.register(Nextel, NextelAdmin)
admin.site.register(Ramal, RamalAdmin)
admin.site.register(Setorramal, SetorramalAdmin)


#admin.site.register(ContaServico)

