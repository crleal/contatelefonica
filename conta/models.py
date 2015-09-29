# -*- coding: utf-8 -*-
from django.db import models

class Filial(models.Model):
    codfilial = models.IntegerField(primary_key=True, db_column = 'codfilial', verbose_name=u'Filial' )
    nome = models.CharField(max_length=30, db_column = 'nome',  verbose_name=u'Nome Filial')

    def __unicode__(self):
        return u'%s - %s' % (self.codfilial, self.nome)

    class Meta:
        db_table = u'filial'


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, db_column = 'nome',  verbose_name=u'Departamento')

    def __unicode__(self):
        return u'%s' % (self.nome)

    class Meta:
        db_table = u'departamento'


class Conta(models.Model):
    num_conta = models.AutoField(primary_key=True, verbose_name=u'Número da conta')
    dt_emissao = models.DateField(verbose_name=u'Emissão')
    dt_inicio = models.DateField(verbose_name='Inicial')
    dt_final = models.DateField(verbose_name='Final')
    dt_vencimento = models.DateField(verbose_name='Vencimento')
    vl_nota = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u'Valor da Nota')
    vlr_ajuste = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u'Valor Ajuste')
    codfilial = models.ForeignKey(Filial, null=True, blank=True, db_column = 'codfilial', verbose_name=u'Filial',)

    def __unicode__(self):
        return  u'%s - %s' % (self.num_conta, self.dt_vencimento )

    class Meta:
        db_table = u'conta'
        permissions = (
             ('listar', 'Listar Contas'),
             ('alterar', 'Alterar Conta'),
             ('incluir', 'Incluir Conta'),
             )


class Numero(models.Model):
    numero_tel = models.IntegerField(primary_key=True, db_column = 'numero_tel',  verbose_name=u'Número Telefone')

    def __unicode__(self):
        return str(self.numero_tel)

    class Meta:
        db_table = u'numeros'


class ContaDetalhe(models.Model):
    id = models.AutoField(primary_key=True)
    num_conta = models.ForeignKey(Conta, db_column='num_conta',  verbose_name=u'Número da conta')
    nun_seq = models.IntegerField( verbose_name=u'Sequência')
    numero_tel = models.ForeignKey(Numero,  db_column = 'numero_tel', verbose_name=u'Telefone')
    tipo = models.IntegerField( verbose_name=u'Tipo')
    dt_lig = models.DateTimeField(verbose_name=u'Data Ligação')
    origem = models.CharField(max_length=30, blank=False,  verbose_name=u'Origem')
    tel_origem = models.CharField(max_length=20,  verbose_name=u'Telefone de Origem')
    destino = models.CharField(max_length=30,  verbose_name=u'Destino')
    tel_destino = models.CharField(max_length=20,  verbose_name=u'Telefone de Destino')
    duracao = models.CharField(verbose_name=u'Duração', max_length=8)
    horario = models.CharField(max_length=30,  verbose_name=u'Horário')
    servico = models.CharField('Serviço', max_length=35)
    vlr_lig = models.DecimalField(max_digits=12, decimal_places=2,  verbose_name=u'Valor da Ligação')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = u'conta_detalhe'
        permissions = (
             ('listar', 'Listar Detalhes de Conta'),
             ('alterar', 'Alterar Detalhe de Conta'),
             ('incluir', 'Incluir Detalhe de Conta'),
             )



class ContaServico(models.Model):
    id = models.AutoField(primary_key=True)
    num_conta = models.ForeignKey(Conta, db_column='num_conta')
    dsc_servico = models.CharField(max_length=30)
    aliq_servico = models.DecimalField(max_digits=12, decimal_places=2)
    vlr_servico = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return u'%s' % (self.dsc_servico)

    class Meta:
        db_table = u'conta_servicos'

class Setorramal(models.Model):
    setorramalid = models.IntegerField(primary_key=True, db_column='setorRamalId') # Field name made lowercase.
    setor = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.setor)

    class Meta:
        db_table = u'setorRamal'
        ordering = ['setor']


class Loja(models.Model):
    lojaid = models.IntegerField(primary_key=True, db_column='lojaId', verbose_name=u'Loja' ) # Field name made lowercase.
    nomeloja = models.CharField(u'Nome Loja', db_column=u'loja', max_length=20, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=120, blank=True)
    bairro = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.IntegerField(null=True, blank=True)
    campovolpe = models.CharField(max_length=10, db_column='campoVolpe', blank=True) # Field name made lowercase.
    criadoem = models.DateTimeField(null=True, db_column='criadoEm', blank=True) # Field name made lowercase.
    alteradoem = models.DateTimeField(db_column='alteradoEm') # Field name made lowercase.
    ativo = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.nomeloja)

    class Meta:
        db_table = u'loja'
        ordering = ['nomeloja']

class Nextel(models.Model):
    nextelid = models.AutoField(primary_key=True, db_column='nextelId') # Field name made lowercase.
    lojaid = models.ForeignKey(Loja, verbose_name= 'Loja', db_column='lojaId',  null=True, blank=True,) # Field name made lowercase.
    setorramalid = models.ForeignKey(Setorramal, verbose_name= 'setor', db_column='setorRamalId', null=True, blank=True,) # Field name made lowercase.
    nome = models.CharField(max_length=100)
    ramal = models.CharField(max_length=100,  null=True, blank=True,)
    id = models.CharField(max_length=100,  null=True, blank=True,)
    celular = models.CharField(max_length=100)
    consulta = models.IntegerField(null=True, blank=True)
 
    def __unicode__(self):
        return u'%s' % (self.nextelid)

    class Meta:
        db_table = u'nextel'
        ordering = ['celular']

class Ramal(models.Model):
    ramalid = models.AutoField(primary_key=True, db_column='ramalId') # Field name made lowercase.
    setorramalid =models.ForeignKey(Setorramal, verbose_name= 'setor', db_column='setorRamalId',  null=True, blank=True,) # Field name made lowercase.
    lojaid = models.ForeignKey(Loja, max_length=300, verbose_name='Loja', db_column='lojaId',  null=True, blank=True,) # Field name made lowercase.
    nome = models.CharField(max_length=100)
    ramal = models.CharField(max_length=100)
    consulta = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.ramal)

    class Meta:
        db_table = u'ramal'
        ordering = ['ramal']
