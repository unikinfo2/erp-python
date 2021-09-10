# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Aliquotasporestado(models.Model):
    idaliquotaestado = models.BigAutoField(db_column='idAliquotaEstado', primary_key=True)  # Field name made lowercase.
    ncm = models.CharField(max_length=8)
    uf = models.CharField(max_length=2)
    mva = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    reducaobaseicms = models.DecimalField(db_column='reducaoBaseIcms', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mvaprodutoimportado = models.DecimalField(db_column='mvaProdutoImportado', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aliquotasporestado'
    def __str__(self):
        return self.ncm



class Boleto(models.Model):
    idboleto = models.BigAutoField(db_column='idBoleto', primary_key=True)  # Field name made lowercase.
    codigobanco = models.BigIntegerField(db_column='codigoBanco', blank=True, null=True)  # Field name made lowercase.
    numeroboleto = models.BigIntegerField(db_column='numeroBoleto', blank=True, null=True)  # Field name made lowercase.
    agencia = models.CharField(max_length=50, blank=True, null=True)
    dtvencimento = models.DateTimeField(db_column='dtVencimento', blank=True, null=True)  # Field name made lowercase.
    dtprocessamento = models.DateTimeField(db_column='dtProcessamento', blank=True, null=True)  # Field name made lowercase.
    dtdocumento = models.DateTimeField(db_column='dtDocumento', blank=True, null=True)  # Field name made lowercase.
    carteira = models.BigIntegerField(blank=True, null=True)
    numerodocumento = models.CharField(db_column='numeroDocumento', max_length=30, blank=True, null=True)  # Field name made lowercase.
    especiedocumento = models.CharField(db_column='especieDocumento', max_length=30, blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=1, blank=True, null=True)
    valorboleto = models.DecimalField(db_column='valorBoleto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tarifacobranca = models.DecimalField(db_column='tarifaCobranca', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outrasdespesas = models.DecimalField(db_column='outrasDespesas', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    jurosdescontocartorio = models.DecimalField(db_column='jurosDescontoCartorio', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    multacobrada = models.DecimalField(db_column='multaCobrada', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    abatimento = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    valorcobrado = models.DecimalField(db_column='valorCobrado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    jurosmora = models.DecimalField(db_column='jurosMora', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outroscreditos = models.DecimalField(db_column='outrosCreditos', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nossonumero = models.CharField(db_column='nossoNumero', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtpagamento = models.DateTimeField(db_column='dtPagamento', blank=True, null=True)  # Field name made lowercase.
    transportado = models.CharField(max_length=1, blank=True, null=True)
    descontoboleto = models.DecimalField(db_column='descontoBoleto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    instruncaoboleto = models.CharField(db_column='instruncaoBoleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    porcentagemmulta = models.DecimalField(db_column='porcentagemMulta', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    porcentagemjurosdiario = models.DecimalField(db_column='porcentagemJurosDiario', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numeropagamento = models.BigIntegerField(db_column='numeroPagamento', blank=True, null=True)  # Field name made lowercase.
    imprimirinstrucoes = models.CharField(db_column='imprimirInstrucoes', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dtdesconto = models.DateTimeField(db_column='dtDesconto', blank=True, null=True)  # Field name made lowercase.
    linknfse = models.CharField(db_column='linkNfse', max_length=200, blank=True, null=True)  # Field name made lowercase.
    emailboleto = models.CharField(db_column='emailBoleto', max_length=500, blank=True, null=True)  # Field name made lowercase.
    reducaovalor = models.DecimalField(db_column='reducaoValor', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    historicoreducao = models.CharField(db_column='historicoReducao', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ultimaremessa = models.CharField(db_column='ultimaRemessa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcedente = models.ForeignKey('Cedente', models.DO_NOTHING, db_column='idCedente', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey('Clifor', models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    iddup = models.ForeignKey('Transacaodup', models.DO_NOTHING, db_column='idDup', blank=True, null=True)  # Field name made lowercase.
    instrucaoboleto = models.CharField(db_column='instrucaoBoleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    instrucaoboleto2 = models.CharField(db_column='instrucaoBoleto2', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boleto'
    def __str__(self):
        return self.dtdocumento

class Cedente(models.Model):
    idcedente = models.BigAutoField(db_column='idCedente', primary_key=True)  # Field name made lowercase.
    carteira = models.CharField(max_length=7, blank=True, null=True)
    instrucao = models.CharField(max_length=250, blank=True, null=True)
    ultimonumero = models.CharField(db_column='ultimoNumero', max_length=30, blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(max_length=10, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    agenciadig = models.CharField(db_column='agenciaDig', max_length=2, blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(max_length=10, blank=True, null=True)
    contadig = models.CharField(db_column='contaDig', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(max_length=10, blank=True, null=True)
    digito = models.CharField(max_length=2, blank=True, null=True)
    codigobanco = models.CharField(db_column='codigoBanco', max_length=20, blank=True, null=True)  # Field name made lowercase.
    arquivonumero = models.BigIntegerField(db_column='arquivoNumero', blank=True, null=True)  # Field name made lowercase.
    quemimprime = models.CharField(db_column='quemImprime', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descricaocedente = models.CharField(db_column='descricaoCedente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idplanocontas = models.ForeignKey('Planocontas', models.DO_NOTHING, db_column='idPlanoContas', blank=True, null=True)  # Field name made lowercase.
    jurosmora = models.DecimalField(db_column='jurosMora', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    multacobrada = models.DecimalField(db_column='multaCobrada', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    imprimeobservacaotransacao = models.CharField(db_column='imprimeObservacaoTransacao', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cedente'
    def __str__(self):
        return self.descricaocedente

class Centrocusto(models.Model):
    idcentrocusto = models.BigAutoField(db_column='idCentroCusto', primary_key=True)  # Field name made lowercase.
    nomecentrocusto = models.CharField(db_column='nomeCentroCusto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    idcentrocustopai = models.ForeignKey('self', models.DO_NOTHING, db_column='idCentroCustoPai', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    contato = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    codigocentrocusto = models.CharField(db_column='codigoCentroCusto', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centrocusto'
    def __str__(self):
        return self.nomecentrocusto

class Clientedoc(models.Model):
    idclientedoc = models.BigAutoField(db_column='idClienteDoc', primary_key=True)  # Field name made lowercase.
    descricaodoc = models.CharField(db_column='descricaoDoc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    observacaodoc = models.CharField(db_column='observacaoDoc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dtdoc = models.DateField(db_column='dtDoc', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey('Clifor', models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    caminhodoc = models.CharField(db_column='caminhoDoc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    prestacaocontas = models.CharField(max_length=1, blank=True, null=True)
    valorreembolso = models.DecimalField(max_digits=12, decimal_places=2)
    idproduto = models.BigIntegerField(db_column='idProduto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientedoc'


class Clifor(models.Model):
    idclifor = models.BigAutoField(db_column='idCliFor', primary_key=True)  # Field name made lowercase.
    codauxiliar = models.CharField(db_column='codAuxiliar', max_length=210, blank=True, null=True)  # Field name made lowercase.
    razaosocial = models.CharField(db_column='razaoSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomefantasia = models.CharField(db_column='nomeFantasia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipopessoa = models.CharField(db_column='tipoPessoa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clientefornecedor = models.CharField(db_column='clienteFornecedor', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpfcnpj = models.CharField(db_column='cpfCnpj', max_length=14, blank=True, null=True)  # Field name made lowercase.
    inscricaoestadual = models.CharField(db_column='inscricaoEstadual', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inscricaomunicipal = models.CharField(db_column='inscricaoMunicipal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigosuframa = models.CharField(db_column='codigoSuframa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=200, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereconumero = models.CharField(db_column='enderecoNumero', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enderecocob = models.CharField(db_column='enderecoCob', max_length=200, blank=True, null=True)  # Field name made lowercase.
    complementocob = models.CharField(db_column='complementoCob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bairrocob = models.CharField(db_column='bairroCob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidadecob = models.CharField(db_column='cidadeCob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cepcob = models.CharField(db_column='cepCob', max_length=8, blank=True, null=True)  # Field name made lowercase.
    enderecoent = models.CharField(db_column='enderecoEnt', max_length=60, blank=True, null=True)  # Field name made lowercase.
    complementoent = models.CharField(db_column='complementoEnt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bairroent = models.CharField(db_column='bairroEnt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidadeent = models.CharField(db_column='cidadeEnt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cepent = models.CharField(db_column='cepEnt', max_length=8, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(max_length=15, blank=True, null=True)
    geramensalidade = models.CharField(db_column='geraMensalidade', max_length=1, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(max_length=300, blank=True, null=True)
    emailnf = models.CharField(db_column='emailNf', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emailboleto = models.CharField(db_column='emailBoleto', max_length=500, blank=True, null=True)  # Field name made lowercase.
    faturarapartirde = models.DateTimeField(db_column='faturarAPartirDe', blank=True, null=True)  # Field name made lowercase.
    faturarate = models.DateTimeField(db_column='faturarAte', blank=True, null=True)  # Field name made lowercase.
    diamensalidade = models.IntegerField(db_column='diaMensalidade', blank=True, null=True)  # Field name made lowercase.
    valormensalidade = models.DecimalField(db_column='valorMensalidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nomeresponsavel1 = models.CharField(db_column='nomeResponsavel1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nomeresponsavel2 = models.CharField(db_column='nomeResponsavel2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dataabertura = models.DateTimeField(db_column='dataAbertura', blank=True, null=True)  # Field name made lowercase.
    clientedesde = models.DateTimeField(db_column='clienteDesde', blank=True, null=True)  # Field name made lowercase.
    observacaonotafiscal = models.CharField(db_column='observacaoNotaFiscal', max_length=250, blank=True, null=True)  # Field name made lowercase.
    calculapis = models.CharField(db_column='calculaPis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculacofins = models.CharField(db_column='calculaCofins', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculacsll = models.CharField(db_column='calculaCsll', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ativoinativo = models.CharField(db_column='ativoInativo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reterimpostos = models.CharField(db_column='reterImpostos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indicereajuste = models.DecimalField(db_column='indiceReajuste', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    uf = models.ForeignKey('Estado', models.DO_NOTHING, related_name='Cliforuf', db_column='uf', blank=True, null=True)
    ufcob = models.ForeignKey('Estado', models.DO_NOTHING, related_name='CliforUFCob', db_column='UFCob', blank=True, null=True)  # Field name made lowercase.
    ufent = models.ForeignKey('Estado', models.DO_NOTHING, related_name='CliforUFEnt', db_column='UFEnt', blank=True, null=True)  # Field name made lowercase.
    idmunicipio = models.ForeignKey('Municipioibge', models.DO_NOTHING, related_name='CliforidMunicipio', db_column='idMunicipio', blank=True, null=True)  # Field name made lowercase.
    idmunicipiocob = models.ForeignKey('Municipioibge', models.DO_NOTHING, related_name='CliforidMunicipiocob', db_column='idMunicipioCob', blank=True, null=True)  # Field name made lowercase.
    idmunicipioent = models.ForeignKey('Municipioibge', models.DO_NOTHING, related_name='CliforidMunicipioent', db_column='idMunicipioEnt', blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey('Paisibge', models.DO_NOTHING, related_name='CliforidPais', db_column='idPais', blank=True, null=True)  # Field name made lowercase.
    idpaiscob = models.ForeignKey('Paisibge', models.DO_NOTHING, related_name='CliforidPaisCob', db_column='idPaisCob', blank=True, null=True)  # Field name made lowercase.
    idpaisent = models.ForeignKey('Paisibge', models.DO_NOTHING, related_name='CliforidPaisEnt', db_column='idPaisEnt', blank=True, null=True)  # Field name made lowercase.
    idtransp = models.ForeignKey('Transportadora', models.DO_NOTHING, db_column='idTransp', blank=True, null=True)  # Field name made lowercase.
    forcarcalcimpostos = models.CharField(db_column='forcarCalcImpostos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=15, blank=True, null=True)
    valoranteriormensalidade = models.DecimalField(db_column='valorAnteriorMensalidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    regimeclifor = models.CharField(db_column='regimeClifor', max_length=15, blank=True, null=True)  # Field name made lowercase.
    paginaguia = models.CharField(db_column='paginaGuia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodesconto = models.CharField(db_column='tipoDesconto', max_length=15, blank=True, null=True)  # Field name made lowercase.
    valordesconto = models.DecimalField(db_column='valorDesconto', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcliforgrupo = models.ForeignKey('self', models.DO_NOTHING, related_name='CliforidCliforGrupo', db_column='idCliforGrupo', blank=True, null=True)  # Field name made lowercase.
    idcontacontrole = models.ForeignKey('Planocontas', models.DO_NOTHING, related_name='CliforidContaControle', db_column='idContaControle', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clifor'
    def __str__(self):
        return '%s - %s' % (self.idclifor, self.razaosocial)


class Cliforcontato(models.Model):
    idcontato = models.BigAutoField(db_column='idContato', primary_key=True)
    nomecontato = models.CharField(db_column='nomeContato', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cargocontato = models.CharField(db_column='cargoContato', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonecontato = models.CharField(db_column='telefoneContato', max_length=20, blank=True, null=True)  # Field name made lowercase.
    celularcontato = models.CharField(db_column='celularContato', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radiocontato = models.CharField(db_column='radioContato', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emailcontato = models.CharField(db_column='emailContato', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ramalcontato = models.CharField(db_column='ramalContato', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deptocontato = models.CharField(db_column='deptoContato', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliforcontato'
    def __str__(self):
        return '%s - %s' % (self.idcontato, self.nomecontato)


class Colaborador(models.Model):
    idcolaborador = models.BigAutoField(db_column='idColaborador', primary_key=True)  # Field name made lowercase.
    admissao = models.DateTimeField(blank=True, null=True)
    demissao = models.DateTimeField(blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    valorhora = models.DecimalField(db_column='valorHora', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantidadehorassemanal = models.DecimalField(db_column='quantidadeHorasSemanal', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nomeusuario = models.CharField(db_column='nomeUsuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senhaacesso = models.CharField(db_column='senhaAcesso', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomecolaborador = models.CharField(db_column='nomeColaborador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    temacolaborador = models.CharField(db_column='temaColaborador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='idDepartamento', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    registroempresa = models.BigIntegerField(db_column='registroEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcentrocusto = models.ForeignKey(Centrocusto, models.DO_NOTHING, db_column='idCentroCusto', blank=True, null=True)  # Field name made lowercase.
    nivelsenha = models.CharField(db_column='nivelSenha', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador'
    def __str__(self):
        return '%s - %s' % (self.idcolaborador, self.nomecolaborador)


class Complementosproduto(models.Model):
    idcomplementosproduto = models.BigAutoField(db_column='idComplementosProduto', primary_key=True)
    produtoprincipal = models.ForeignKey('Produto', models.DO_NOTHING, related_name='ComplementosprodutoprodutoPrincipal', db_column='produtoPrincipal')  # Field name made lowercase.
    produtocomplemento = models.ForeignKey('Produto', models.DO_NOTHING, related_name='ComplementosprodutoprodutoComplemento', db_column='produtoComplemento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complementosproduto'


class Configdre(models.Model):
    iddre = models.BigAutoField(db_column='idDRE', primary_key=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    titulodre = models.CharField(db_column='tituloDRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcontainiciodre = models.ForeignKey('Planocontas', models.DO_NOTHING, related_name='ConfigdreidContaInicioDRE', db_column='idContaInicioDRE', blank=True, null=True)  # Field name made lowercase.
    idcontafimdre = models.ForeignKey('Planocontas', models.DO_NOTHING, related_name='ConfigdreidContaFimDRE', db_column='idContaFimDRE', blank=True, null=True)  # Field name made lowercase.
    tipoimpressaodre = models.CharField(db_column='tipoImpressaoDRE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valordre = models.DecimalField(db_column='valorDRE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    formuladre = models.CharField(db_column='formulaDRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcontasdre = models.CharField(db_column='idContasDRE', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configdre'


class Configncm(models.Model):
    idncm = models.BigAutoField(db_column='idNcm', primary_key=True)  # Field name made lowercase.
    ncm = models.CharField(max_length=8)
    descricaoncm = models.CharField(db_column='descricaoNcm', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.DecimalField(db_column='aliqIpi', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqleitransparencia = models.DecimalField(db_column='aliqLeiTransparencia', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cest = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configncm'
    def __str__(self):
        return '%s - %s' % (self.ncm, self.descricaoncm)


class Configtransacaonf(models.Model):
    idconfigtransacaonf = models.BigAutoField(db_column='idConfigTransacaoNF', primary_key=True)  # Field name made lowercase.
    idtipotransacaonf = models.BigIntegerField(db_column='idTipoTransacaoNF')  # Field name made lowercase.
    ncm = models.CharField(max_length=8)
    cstnormal = models.CharField(db_column='cstNormal', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstreducaobase = models.CharField(db_column='cstReducaoBase', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstst = models.CharField(db_column='cstST', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cststrb = models.CharField(db_column='cstSTRB', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='cstIpi', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='cstPis', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='cstCofins', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstcsll = models.CharField(db_column='cstCsll', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cfopestado = models.CharField(db_column='cfopEstado', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopestadost = models.CharField(db_column='cfopEstadoST', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopforaestado = models.CharField(db_column='cfopForaEstado', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopforaestadost = models.CharField(db_column='cfopForaEstadoST', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopexterior = models.CharField(db_column='cfopExterior', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopestadoproducao = models.CharField(db_column='cfopEstadoProducao', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopestadoconsumo = models.CharField(db_column='cfopEstadoConsumo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopforaestadoproducao = models.CharField(db_column='cfopForaEstadoProducao', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopforaestadoconsumo = models.CharField(db_column='cfopForaEstadoConsumo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopestadoconsumopp = models.CharField(db_column='cfopEstadoConsumoPP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cfopforaestadoconsumopp = models.CharField(db_column='cfopForaEstadoConsumoPP', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configtransacaonf'


class Configuracao(models.Model):
    chave = models.CharField(db_column='CHAVE', primary_key=True, max_length=50)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100)  # Field name made lowercase.
    valor = models.CharField(db_column='VALOR', max_length=240, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configuracao'
        unique_together = (('chave', 'descricao'),)


class Controleafastamento(models.Model):
    idcontroleafastamento = models.BigAutoField(db_column='idcontroleAfastamento', primary_key=True)  # Field name made lowercase.
    idcolaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='idColaborador')  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa')  # Field name made lowercase.
    datainicioafastamento = models.DateField(db_column='dataInicioAfastamento', blank=True, null=True)  # Field name made lowercase.
    tipoafastamento = models.CharField(db_column='tipoAfastamento', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(max_length=20, blank=True, null=True)
    numerobeneficio = models.CharField(db_column='numeroBeneficio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datapericia = models.DateField(db_column='dataPericia', blank=True, null=True)  # Field name made lowercase.
    dataconcecaoate = models.DateField(db_column='dataConcecaoAte', blank=True, null=True)  # Field name made lowercase.
    datanovapericia = models.DateField(db_column='dataNovaPericia', blank=True, null=True)  # Field name made lowercase.
    dataindeferimento = models.DateField(db_column='dataIndeferimento', blank=True, null=True)  # Field name made lowercase.
    dataalta = models.DateField(db_column='dataAlta', blank=True, null=True)  # Field name made lowercase.
    tipoalta = models.CharField(db_column='tipoAlta', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ocorrenciasafastamento = models.TextField(db_column='ocorrenciasAfastamento', blank=True, null=True)  # Field name made lowercase.
    dataultimaalteracao = models.DateTimeField(db_column='dataUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    quemalterou = models.CharField(db_column='quemAlterou', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'controleafastamento'


class Customfield(models.Model):
    idcustomfield = models.BigAutoField(db_column='idCustomField', primary_key=True)  # Field name made lowercase.
    nomecustomfield = models.CharField(db_column='nomeCustomField', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tipocustomfield = models.CharField(db_column='tipoCustomField', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tamanhocustomfield = models.IntegerField(db_column='tamanhoCustomField', blank=True, null=True)  # Field name made lowercase.
    nomeclasse = models.CharField(db_column='nomeClasse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customfield'


class Departamento(models.Model):
    iddepartamento = models.BigAutoField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nomedepartamento = models.CharField(db_column='nomeDepartamento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'
    def __str__(self):
        return '%s - %s' % (self.iddepartamento, self.nomedepartamento)


class Diario(models.Model):
    iddiario = models.BigAutoField(db_column='idDiario', primary_key=True)  # Field name made lowercase.
    historicodebito = models.CharField(db_column='historicoDebito', max_length=200, blank=True, null=True)  # Field name made lowercase.
    historicocredito = models.CharField(db_column='historicoCredito', max_length=200, blank=True, null=True)  # Field name made lowercase.
    documento = models.CharField(max_length=45, blank=True, null=True)
    dtlancamento = models.DateTimeField(db_column='dtLancamento', blank=True, null=True)  # Field name made lowercase.
    dtdocumento = models.DateTimeField(db_column='dtDocumento', blank=True, null=True)  # Field name made lowercase.
    valorlancto = models.DecimalField(db_column='valorLancto', max_digits=15, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    iddocumento = models.IntegerField(db_column='idDocumento', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.IntegerField(db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcontadeb = models.ForeignKey('Planocontas', models.DO_NOTHING, related_name='idContaDeb', db_column='idContaDeb', blank=True, null=True)  # Field name made lowercase.
    idcontacred = models.ForeignKey('Planocontas', models.DO_NOTHING, related_name='idContaCred', db_column='idContaCred', blank=True, null=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey('Transacao', models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.
    idtransacaoimposto = models.ForeignKey('Transacaoimposto', models.DO_NOTHING, db_column='idTransacaoImposto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diario'

class Dre(models.Model):
    iddre = models.BigAutoField(db_column='idDre', primary_key=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcolaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='idColaborador', blank=True, null=True)  # Field name made lowercase.
    idconta = models.ForeignKey('Planocontas', models.DO_NOTHING, db_column='idConta', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=100, blank=True, null=True)
    valor1 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor2 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor3 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor4 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor5 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor6 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor7 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor8 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor9 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor10 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor11 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor12 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    valor13 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dre'


class Empresa(models.Model):
    idempresa = models.BigAutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    razaoemp = models.CharField(db_column='razaoEmp', max_length=70, blank=True, null=True)  # Field name made lowercase.
    nomefantasiaemp = models.CharField(db_column='nomeFantasiaEmp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enderecoemp = models.CharField(db_column='enderecoEmp', max_length=60, blank=True, null=True)  # Field name made lowercase.
    complend = models.CharField(db_column='complEnd', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numeroend = models.CharField(db_column='numeroEnd', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cepemp = models.CharField(db_column='cepEmp', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidadeemp = models.CharField(db_column='cidadeEmp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigomunicipioemp = models.CharField(db_column='codigoMunicipioEmp', max_length=8, blank=True, null=True)  # Field name made lowercase.
    emailemp = models.CharField(db_column='emailEmp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteemp = models.CharField(db_column='siteEmp', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tppessoa = models.CharField(db_column='tpPessoa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpjemp = models.CharField(db_column='cnpjEmp', max_length=14, blank=True, null=True)  # Field name made lowercase.
    iestemp = models.CharField(db_column='iEstEmp', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ccmemp = models.CharField(db_column='ccmEmp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fone1emp = models.CharField(db_column='fone1Emp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fone2emp = models.CharField(db_column='fone2Emp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fone3emp = models.CharField(db_column='fone3Emp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fone4emp = models.CharField(db_column='fone4Emp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    faxemp = models.CharField(db_column='faxEmp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ufemp = models.ForeignKey('Estado', models.DO_NOTHING, db_column='UFEmp', blank=True, null=True)  # Field name made lowercase.
    caminhologo = models.ImageField(upload_to='images')  # Field name made lowercase.
    codigoaux = models.CharField(db_column='codigoAux', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caminhologosecundario = models.ImageField(upload_to='images')  # Field name made lowercase.
    tprelpv = models.CharField(db_column='tpRelPv', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idempresamatriz = models.BigIntegerField(db_column='idEmpresaMatriz', blank=True, null=True)  # Field name made lowercase.
    verestoquematriz = models.CharField(db_column='verEstoqueMatriz', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vercliformatriz = models.CharField(db_column='verCliForMatriz', max_length=1, blank=True, null=True)  # Field name made lowercase.
    regimeempresa = models.CharField(db_column='regimeEmpresa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    percdifaldestino = models.DecimalField(db_column='percDifalDestino', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    percdifalorigem = models.DecimalField(db_column='percDifalOrigem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cnaeemp = models.CharField(db_column='cnaeEmp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bairroemp = models.CharField(db_column='bairroEmp', max_length=60, blank=True, null=True)  # Field name made lowercase.
    editaautorizada = models.CharField(db_column='editaAutorizada', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxaentrega = models.DecimalField(db_column='taxaEntrega', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'
    def __str__(self):
        return '%s - %s' % (self.idempresa, self.razaoemp)

class Estado(models.Model):
    uf = models.CharField(primary_key=True, max_length=3)
    nomeuf = models.CharField(db_column='nomeUf', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aliqinterestadual = models.DecimalField(db_column='aliqInterestadual', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqst = models.DecimalField(db_column='aliqSt', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqdentroestado = models.DecimalField(db_column='aliqDentroEstado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqimportado1 = models.DecimalField(db_column='aliqImportado1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqimportado2 = models.DecimalField(db_column='aliqImportado2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqfcp = models.DecimalField(db_column='aliqFcp', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codigouf = models.CharField(db_column='codigoUF', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'
    def __str__(self):
        return '%s - %s' % (self.uf, self.nomeuf)


class Estagiotransacao(models.Model):
    idestagiotransacao = models.BigAutoField(db_column='idEstagioTransacao', primary_key=True)  # Field name made lowercase.
    nomeestagio = models.CharField(db_column='nomeEstagio', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estagiotransacao'
    def __str__(self):
        return '%s - %s' % (self.idestagiotransacao, self.nomeestagio)


class Estoque(models.Model):
    idestoque = models.BigAutoField(db_column='idEstoque', primary_key=True)  # Field name made lowercase.
    cepestoque = models.CharField(db_column='cepEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cidadeestoque = models.CharField(db_column='cidadeEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigoauxestoque = models.CharField(db_column='codigoAuxEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    complestoque = models.CharField(db_column='complEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailestoque = models.CharField(db_column='emailEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enderecoestoque = models.CharField(db_column='enderecoEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faxestoque = models.CharField(db_column='faxEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fone1estoque = models.CharField(db_column='fone1Estoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fone2estoque = models.CharField(db_column='fone2Estoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fone3estoque = models.CharField(db_column='fone3Estoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fone4estoque = models.CharField(db_column='fone4Estoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomeestoque = models.CharField(db_column='nomeEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numeroestoque = models.CharField(db_column='numeroEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    ufestoque = models.ForeignKey(Estado, models.DO_NOTHING, db_column='UFEstoque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estoque'
    def __str__(self):
        return '%s - %s' % (self.idestoque, self.nomeestoque)


class Estoqueitens(models.Model):
    idestoqueitem = models.BigAutoField(db_column='idEstoqueItem', primary_key=True)  # Field name made lowercase.
    quantidadeajuste = models.DecimalField(db_column='quantidadeAjuste', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tpmovimentoestoque = models.CharField(db_column='tpMovimentoEstoque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idestoque = models.ForeignKey(Estoque, models.DO_NOTHING, db_column='idEstoque', blank=True, null=True)  # Field name made lowercase.
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='idProduto', blank=True, null=True)  # Field name made lowercase.
    idtransacaoitem = models.ForeignKey('Transacaoitem', models.DO_NOTHING, db_column='idTransacaoItem', blank=True, null=True)  # Field name made lowercase.
    datamovimentacao = models.DateTimeField(db_column='dataMovimentacao', blank=True, null=True)  # Field name made lowercase.
    motivoajuste = models.CharField(db_column='motivoAjuste', max_length=50, blank=True, null=True)  # Field name made lowercase.
    saldoanterior = models.DecimalField(db_column='saldoAnterior', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldoatual = models.DecimalField(db_column='saldoAtual', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estoqueitens'


class Extrato(models.Model):
    idextrato = models.BigAutoField(db_column='idExtrato', primary_key=True)  # Field name made lowercase.
    data_movto = models.DateTimeField(blank=True, null=True)
    historico_movto = models.CharField(max_length=250, blank=True, null=True)
    idextratoparamentro = models.ForeignKey('Extratoparametro', models.DO_NOTHING, db_column='idExtratoParamentro', blank=True, null=True)  # Field name made lowercase.
    valor_lancto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    statusextrato = models.CharField(db_column='statusExtrato', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extrato'


class Extratoparametro(models.Model):
    idextratoparamentro = models.BigAutoField(db_column='idExtratoParamentro', primary_key=True)  # Field name made lowercase.
    historicomovto = models.CharField(db_column='historicoMovto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    contacontrapartida = models.ForeignKey('Planocontas', models.DO_NOTHING, db_column='contaContraPartida', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extratoparametro'


class Fpagto(models.Model):
    idfpagto = models.BigAutoField(db_column='idFPagto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=40, blank=True, null=True)
    dupapartir = models.CharField(db_column='dupApartir', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.BigIntegerField(db_column='idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fpagto'
    def __str__(self):
        return '%s - %s' % (self.idfpagto, self.descricao)


class Fpagtoitem(models.Model):
    idfpagtoitem = models.BigAutoField(db_column='idFPagtoItem', primary_key=True)  # Field name made lowercase.
    qtdedias = models.IntegerField(db_column='qtdeDias', blank=True, null=True)  # Field name made lowercase.
    percentualparc = models.DecimalField(db_column='percentualParc', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idfpagto = models.ForeignKey(Fpagto, models.DO_NOTHING, db_column='idFPagto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fpagtoitem'


class Log(models.Model):
    idlog = models.BigAutoField(db_column='idLog', primary_key=True)  # Field name made lowercase.
    modulolog = models.CharField(db_column='moduloLog', max_length=45)  # Field name made lowercase.
    idmodulo = models.IntegerField(db_column='idModulo', blank=True, null=True)  # Field name made lowercase.
    acaolog = models.CharField(db_column='acaoLog', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datahoralog = models.DateTimeField(db_column='datahoraLog')  # Field name made lowercase.
    idcolaboradorlog = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='idColaboradorLog', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log'


class Menu(models.Model):
    idmenu = models.BigAutoField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    nomeopcao = models.CharField(db_column='nomeOpcao', max_length=100)  # Field name made lowercase.
    nomeicone = models.CharField(db_column='nomeIcone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=100, blank=True, null=True)
    idmenuprincipal = models.ForeignKey('self', models.DO_NOTHING, db_column='idMenuPrincipal', blank=True, null=True)  # Field name made lowercase.
    modulo = models.CharField(max_length=45, blank=True, null=True)
    descricaobundle = models.CharField(db_column='descricaoBundle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    menuordem = models.CharField(db_column='menuOrdem', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'
    def __str__(self):
        return '%s - %s' % (self.idmenu, self.nomeopcao)


class Menucolaborador(models.Model):
    idmenucolaborador = models.BigAutoField(db_column='idMenuColaborador', primary_key=True)  # Field name made lowercase.
    idcolaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='idColaborador', blank=True, null=True)  # Field name made lowercase.
    idmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='idMenu', blank=True, null=True)  # Field name made lowercase.
    direitos = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menucolaborador'


class Municipioibge(models.Model):
    idmunicipio = models.BigIntegerField(db_column='idMunicipio', primary_key=True)  # Field name made lowercase.
    nomemunicipio = models.CharField(db_column='nomeMunicipio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ufmunicipio = models.CharField(db_column='ufMunicipio', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipioibge'
    def __str__(self):
        return '%s - %s - %s' % (self.ufmunicipio, self.idmunicipio, self.nomemunicipio)


class Ocorrenciaprocesso(models.Model):
    idocorrencia = models.BigAutoField(db_column='idOcorrencia', primary_key=True)  # Field name made lowercase.
    dtocorrencia = models.DateTimeField(db_column='dtOcorrencia', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=150, blank=True, null=True)
    idprocesso = models.ForeignKey('Processos', models.DO_NOTHING, db_column='idProcesso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ocorrenciaprocesso'


class Operacao(models.Model):
    codigooperacao = models.CharField(db_column='codigoOperacao', primary_key=True, max_length=6)  # Field name made lowercase.
    descricao = models.CharField(max_length=40, blank=True, null=True)
    compoeipi = models.CharField(db_column='compoeIpi', max_length=1, blank=True, null=True)  # Field name made lowercase.
    compoeicms = models.CharField(db_column='compoeIcms', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exportaoperacao = models.CharField(db_column='exportaOperacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pagacomissao = models.CharField(db_column='pagaComissao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    observacaooperacao = models.CharField(db_column='observacaoOperacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    refoperacao = models.CharField(db_column='refOperacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calculapis = models.CharField(db_column='calculaPis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculacofins = models.CharField(db_column='calculaCofins', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculacsll = models.CharField(db_column='calculaCsll', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculaipi = models.CharField(db_column='calculaIpi', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculaicms = models.CharField(db_column='calculaIcms', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculast = models.CharField(db_column='calculaST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bonificacao = models.CharField(max_length=1, blank=True, null=True)
    calculairpj = models.CharField(db_column='calculaIrpj', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calculaiss = models.CharField(db_column='calculaIss', max_length=1, blank=True, null=True)  # Field name made lowercase.
    operacaocontrapartida = models.CharField(db_column='operacaoContraPartida', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='cstPis', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='cstCofins', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='cstIpi', max_length=4, blank=True, null=True)  # Field name made lowercase.
    templateqb = models.CharField(db_column='templateQB', max_length=100, blank=True, null=True)  # Field name made lowercase.
    somarfretebaseipi = models.CharField(db_column='somarFreteBaseIpi', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aliqpis = models.DecimalField(db_column='aliqPis', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqcofins = models.DecimalField(db_column='aliqCofins', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqcsll = models.DecimalField(db_column='aliqCsll', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    venda = models.CharField(max_length=1, blank=True, null=True)
    aliqirf = models.DecimalField(db_column='aliqIRF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqiss = models.DecimalField(db_column='aliqISS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codservico = models.CharField(db_column='codServico', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pisocalcirf = models.DecimalField(db_column='pisoCalcIrf', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pisocalcpiscofinscsll = models.DecimalField(db_column='pisoCalcPisCofinsCsll', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    percleitransp = models.DecimalField(db_column='percLeiTransp', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idcontadebito = models.BigIntegerField(db_column='idContaDebito', blank=True, null=True)  # Field name made lowercase.
    idcontacredito = models.BigIntegerField(db_column='idContaCredito', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.BigIntegerField(db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcontarecebivel = models.BigIntegerField(db_column='idContaRecebivel', blank=True, null=True)  # Field name made lowercase.
    idcontareceita = models.BigIntegerField(db_column='idContaReceita', blank=True, null=True)  # Field name made lowercase.
    idtipotransacaonf = models.BigIntegerField(db_column='idTipoTransacaoNF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operacao'
    def __str__(self):
        return '%s - %s' % (self.codigooperacao, self.descricao)


class Operacaoimposto(models.Model):
    idoperacaoimposto = models.BigAutoField(db_column='idOperacaoImposto', primary_key=True)  # Field name made lowercase.
    contadebitooperacaoimposto = models.BigIntegerField(db_column='contaDebitoOperacaoImposto', blank=True, null=True)  # Field name made lowercase.
    contacreditooperacaoimposto = models.BigIntegerField(db_column='contaCreditoOperacaoImposto', blank=True, null=True)  # Field name made lowercase.
    codigooperacao = models.CharField(db_column='codigoOperacao', max_length=6)  # Field name made lowercase.
    idtipoimposto = models.BigIntegerField(db_column='idTipoImposto')  # Field name made lowercase.
    aliqoperacaoimposto = models.DecimalField(db_column='aliqOperacaoImposto', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    idclifor = models.BigIntegerField(db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operacaoimposto'


class Ordemdespacho(models.Model):
    idordemdespacho = models.BigAutoField(db_column='idOrdemDespacho', primary_key=True)  # Field name made lowercase.
    dtenvio = models.DateTimeField(db_column='dtEnvio', blank=True, null=True)  # Field name made lowercase.
    idtransp = models.ForeignKey('Transportadora', models.DO_NOTHING, db_column='idTransp', blank=True, null=True)  # Field name made lowercase.
    motorista = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    placa = models.CharField(max_length=45, blank=True, null=True)
    idtransacao = models.ForeignKey('Transacao', models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.
    precocubado = models.DecimalField(db_column='precoCubado', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalfrete = models.DecimalField(db_column='totalFrete', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcubado = models.DecimalField(db_column='totalCubado', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itensconferidos = models.CharField(db_column='itensConferidos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    percfretesobrenota = models.DecimalField(db_column='percFreteSobreNota', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordemdespacho'


class Ordemdespachoitem(models.Model):
    iddespachoitem = models.BigAutoField(db_column='idDespachoItem', primary_key=True)  # Field name made lowercase.
    idordemdespacho = models.ForeignKey(Ordemdespacho, models.DO_NOTHING, db_column='idOrdemDespacho')  # Field name made lowercase.
    volume = models.BigIntegerField(blank=True, null=True)
    dim1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dim2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dim3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pesocubado = models.DecimalField(db_column='pesoCubado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordemdespachoitem'


class Paisibge(models.Model):
    idpais = models.BigIntegerField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    nomepais = models.CharField(db_column='nomePais', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codpais4r = models.CharField(db_column='codPais4R', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paisibge'
    def __str__(self):
        return '%s - %s' % (self.idpais, self.nomepais)


class Perfil(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    perfil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'


class Planocontas(models.Model):
    idconta = models.BigAutoField(db_column='idConta', primary_key=True)  # Field name made lowercase.
    codconta = models.CharField(db_column='codConta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descconta = models.CharField(db_column='descConta', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tipoconta = models.CharField(db_column='tipoConta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ativaconta = models.CharField(db_column='ativaConta', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcontaprincipal = models.ForeignKey('self', models.DO_NOTHING, related_name='idContaPrincipal', db_column='idContaPrincipal', blank=True, null=True)  # Field name made lowercase.
    contaclassificacao = models.CharField(db_column='contaClassificacao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contapara = models.CharField(db_column='contaPara', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planocontas'
    def __str__(self):
        return '%s - %s' % (self.codconta, self.descconta)


class Prj4(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'prj4'


class Processos(models.Model):
    idprocesso = models.BigAutoField(db_column='idProcesso', primary_key=True)  # Field name made lowercase.
    idcolaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='idColaborador', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(max_length=150, blank=True, null=True)
    statusatendimento = models.CharField(db_column='statusAtendimento', max_length=15, blank=True, null=True)  # Field name made lowercase.
    prioridade = models.CharField(max_length=15, blank=True, null=True)
    dataabertura = models.DateTimeField(db_column='dataAbertura')  # Field name made lowercase.
    descricao = models.CharField(max_length=150, blank=True, null=True)
    relatocliforoperador = models.CharField(db_column='relatoCliforOperador', max_length=400, blank=True, null=True)  # Field name made lowercase.
    geracobranca = models.CharField(db_column='geraCobranca', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipoatendimento = models.CharField(db_column='tipoAtendimento', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtinicio = models.DateTimeField(db_column='dtInicio')  # Field name made lowercase.
    dtprevistafechamento = models.DateTimeField(db_column='dtPrevistaFechamento')  # Field name made lowercase.
    dtfechamento = models.DateTimeField(db_column='dtFechamento')  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa')  # Field name made lowercase.
    nomeclifor = models.CharField(db_column='nomeClifor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cpfcpnj = models.CharField(db_column='cpfCpnj', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpfcnpj = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processos'


class Produto(models.Model):
    idproduto = models.BigAutoField(db_column='idProduto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=500, blank=True, null=True)
    codigoaux = models.CharField(db_column='codigoAux', max_length=250, blank=True, null=True)  # Field name made lowercase.
    compldescricao = models.CharField(db_column='complDescricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tpproduto = models.CharField(db_column='tpProduto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    destinacao = models.CharField(max_length=1, blank=True, null=True)
    pesobruto = models.DecimalField(db_column='pesoBruto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    markup = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantidadeatual = models.DecimalField(db_column='quantidadeAtual', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precocusto = models.DecimalField(db_column='precoCusto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='precoVenda', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tpitem = models.CharField(db_column='tpItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pesa = models.CharField(max_length=1, blank=True, null=True)
    customedio = models.DecimalField(db_column='custoMedio', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precomedio = models.DecimalField(db_column='precoMedio', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estoqueminimo = models.DecimalField(db_column='estoqueMinimo', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estoquemaximo = models.DecimalField(db_column='estoqueMaximo', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pesoliquido = models.DecimalField(db_column='pesoLiquido', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codigobarras = models.CharField(db_column='codigoBarras', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descricao2 = models.CharField(max_length=500, blank=True, null=True)
    descricao3 = models.CharField(max_length=500, blank=True, null=True)
    forcarcb = models.CharField(db_column='forcarCB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    codunimed = models.ForeignKey('Unidademedida', models.DO_NOTHING, db_column='codUniMed', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(max_length=8, blank=True, null=True)
    origem = models.CharField(max_length=2, blank=True, null=True)
    fabricacaopropria = models.CharField(db_column='fabricacaoPropria', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qtddiasgarantia = models.IntegerField(db_column='qtdDiasGarantia', blank=True, null=True)  # Field name made lowercase.
    grupoproduto = models.ForeignKey('self', models.DO_NOTHING, db_column='grupoProduto', blank=True, null=True)  # Field name made lowercase.
    caminhoimagem = models.ImageField(upload_to='images')  # Field name made lowercase.
    descricaocompleta = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'
    def __str__(self):
        return '%s - %s' % (self.idproduto, self.descricao)


class Produtoadicional(models.Model):
    idadicional = models.BigAutoField(db_column='idAdicional', primary_key=True)  # Field name made lowercase.
    idprodutoorigem = models.BigIntegerField(db_column='idProdutoOrigem')  # Field name made lowercase.
    idprodutoadicionavel = models.BigIntegerField(db_column='idProdutoAdicionavel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtoadicional'


class Produtosdespachados(models.Model):
    idprodutosdespachados = models.BigAutoField(db_column='idProdutosDespachados', primary_key=True)  # Field name made lowercase.
    idordemdespacho = models.ForeignKey(Ordemdespacho, models.DO_NOTHING, db_column='idOrdemDespacho')  # Field name made lowercase.
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='idProduto')  # Field name made lowercase.
    quantidadedespacho = models.DecimalField(db_column='quantidadeDespacho', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosdespachados'


class Projeto(models.Model):
    idprojeto = models.BigAutoField(db_column='idProjeto', primary_key=True)  # Field name made lowercase.
    nomeprojeto = models.CharField(db_column='nomeProjeto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateTimeField(db_column='dataInicio')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='dataFinal', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    statusprojeto = models.CharField(db_column='statusProjeto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valororcado = models.DecimalField(db_column='valorOrcado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dataconclusao = models.DateTimeField(db_column='dataConclusao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projeto'
    def __str__(self):
        return '%s - %s' % (self.idprojeto, self.nomeprojeto)


class Relatorio(models.Model):
    idrelatorio = models.BigAutoField(db_column='idRelatorio', primary_key=True)  # Field name made lowercase.
    campogrupo = models.CharField(db_column='campoGrupo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campoordem = models.CharField(db_column='campoOrdem', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campototalizar = models.CharField(db_column='campoTotalizar', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nomerelatorio = models.CharField(db_column='nomeRelatorio', max_length=60, blank=True, null=True)  # Field name made lowercase.
    orientacaorelatorio = models.CharField(db_column='orientacaoRelatorio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateTimeField(blank=True, null=True)
    datafinal = models.DateTimeField(db_column='dataFinal', blank=True, null=True)  # Field name made lowercase.
    imprimeitens = models.CharField(db_column='imprimeItens', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imprimeimpostos = models.CharField(db_column='imprimeImpostos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    imprimecontas = models.CharField(db_column='imprimeContas', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatorio'
    def __str__(self):
        return '%s - %s' % (self.idrelatorio, self.nomerelatorio)


class Relatoriocampo(models.Model):
    idrelatoriocampo = models.BigAutoField(db_column='idRelatorioCampo', primary_key=True)  # Field name made lowercase.
    idrelatorio = models.ForeignKey(Relatorio, models.DO_NOTHING, db_column='idRelatorio')  # Field name made lowercase.
    camporelatorio = models.CharField(db_column='campoRelatorio', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tamanhocampo = models.IntegerField(db_column='tamanhoCampo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatoriocampo'


class Relatoriofiltro(models.Model):
    idrelatoriofiltro = models.BigAutoField(db_column='idRelatorioFiltro', primary_key=True)  # Field name made lowercase.
    idrelatorio = models.ForeignKey(Relatorio, models.DO_NOTHING, db_column='idRelatorio')  # Field name made lowercase.
    camporelatorio = models.CharField(db_column='campoRelatorio', max_length=60, blank=True, null=True)  # Field name made lowercase.
    condicaorelatorio = models.CharField(db_column='condicaoRelatorio', max_length=5, blank=True, null=True)  # Field name made lowercase.
    conteudorelatorio = models.CharField(db_column='conteudoRelatorio', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatoriofiltro'


class Representante(models.Model):
    idrepre = models.BigAutoField(db_column='idRepre', primary_key=True)  # Field name made lowercase.
    comissaorepre = models.DecimalField(db_column='comissaoRepre', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    obsrepre = models.CharField(db_column='obsRepre', max_length=250, blank=True, null=True)  # Field name made lowercase.
    comissaogerente = models.DecimalField(db_column='comissaoGerente', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ativorepre = models.CharField(db_column='ativoRepre', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enderecorepre = models.CharField(db_column='enderecoRepre', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cidaderepre = models.CharField(db_column='cidadeRepre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bairrorepre = models.CharField(db_column='bairroRepre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ceprepre = models.CharField(db_column='cepRepre', max_length=8, blank=True, null=True)  # Field name made lowercase.
    numerorepre = models.CharField(db_column='numeroRepre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailrepre = models.CharField(db_column='emailRepre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonerepre = models.CharField(db_column='telefoneRepre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nomerepre = models.CharField(db_column='nomeRepre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apelidorepre = models.CharField(db_column='apelidoRepre', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    ufrepre = models.ForeignKey(Estado, models.DO_NOTHING, db_column='UFRepre', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    idcontadebito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='RepresentanteidContaDebito', db_column='idContaDebito', blank=True, null=True)  # Field name made lowercase.
    idcontacredito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='RepresentanteidContaCredito', db_column='idContaCredito', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'representante'
    def __str__(self):
        return '%s - %s - %s' % (self.idrepre, self.nomerepre, self.apelidorepre)


class Saldoconta(models.Model):
    idsaldoconta = models.BigAutoField(db_column='idSaldoConta', primary_key=True)  # Field name made lowercase.
    anomessaldo = models.CharField(db_column='anomesSaldo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idcontasaldo = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='idContaSaldo', db_column='idContaSaldo', blank=True, null=True)  # Field name made lowercase.
    saldoanterior = models.DecimalField(db_column='saldoAnterior', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tpsaldoanterior = models.CharField(db_column='tpSaldoAnterior', max_length=1, blank=True, null=True)  # Field name made lowercase.
    valordebito = models.DecimalField(db_column='valorDebito', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valorcredito = models.DecimalField(db_column='valorCredito', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.DecimalField(db_column='SaldoFinal', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tpsaldofinal = models.CharField(db_column='tpSaldoFinal', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saldoconta'


class Sequence(models.Model):
    seq_name = models.CharField(db_column='SEQ_NAME', primary_key=True, max_length=50)  # Field name made lowercase.
    seq_count = models.DecimalField(db_column='SEQ_COUNT', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sequence'
    def __str__(self):
        return '%s - %s' % (self.seq_name, self.seq_count)


class Sequencia(models.Model):
    idsequencia = models.BigAutoField(db_column='idSequencia', primary_key=True)
    nomesequencia = models.CharField(max_length=45, blank=True, null=True)
    valorsequencia = models.BigIntegerField(blank=True, null=True)
    prefixosequencia = models.CharField(max_length=10, blank=True, null=True)
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sequencia'
    def __str__(self):
        return '%s - %s - %s' % (self.idsequencia, self.nomesequencia, self.valorsequencia)


class Tabelasimples(models.Model):
    cod_tabsimples = models.BigAutoField(db_column='COD_TABSIMPLES', primary_key=True)  # Field name made lowercase.
    receita1_tabsimples = models.DecimalField(db_column='RECEITA1_TABSIMPLES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    receita2_tabsimples = models.DecimalField(db_column='RECEITA2_TABSIMPLES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_simples = models.DecimalField(db_column='ALIQ_SIMPLES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_irpj = models.DecimalField(db_column='ALIQ_IRPJ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_csll = models.DecimalField(db_column='ALIQ_CSLL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_cofins = models.DecimalField(db_column='ALIQ_COFINS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_pis = models.DecimalField(db_column='ALIQ_PIS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_cpp = models.DecimalField(db_column='ALIQ_CPP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_ipi = models.DecimalField(db_column='ALIQ_IPI', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabelasimples'


class Tipoimposto(models.Model):
    idtipoimposto = models.BigAutoField(db_column='idTipoImposto', primary_key=True)  # Field name made lowercase.
    nometipoimposto = models.CharField(db_column='nomeTipoImposto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    calcularimpostoapartirde = models.DecimalField(db_column='calcularImpostoAPartirDe', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reternaoreter = models.CharField(db_column='reterNaoReter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ordemcalculo = models.IntegerField(db_column='ordemCalculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoimposto'
    def __str__(self):
        return '%s - %s' % (self.idtipoimposto, self.nometipoimposto)


class Tipotransacaonf(models.Model):
    idtipotransacaonf = models.BigAutoField(db_column='idTipoTransacaoNF', primary_key=True)  # Field name made lowercase.
    descricaotipotransacaonf = models.CharField(db_column='descricaoTipoTransacaoNf', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.BigIntegerField(db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipotransacaonf'
    def __str__(self):
        return '%s - %s' % (self.idtipotransacaonf, self.descricaotipotransacaonf)


class Transacao(models.Model):
    idtransacao = models.BigAutoField(db_column='idTransacao', primary_key=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    idprojeto = models.ForeignKey(Projeto, models.DO_NOTHING, db_column='idProjeto', blank=True, null=True)  # Field name made lowercase.
    idtransp = models.ForeignKey('Transportadora', models.DO_NOTHING, db_column='idTransp', blank=True, null=True)  # Field name made lowercase.
    idrepre = models.ForeignKey(Representante, models.DO_NOTHING, db_column='idRepre', blank=True, null=True)  # Field name made lowercase.
    idfpagto = models.ForeignKey(Fpagto, models.DO_NOTHING, db_column='idFPagto', blank=True, null=True)  # Field name made lowercase.
    idtransacaoorigem = models.ForeignKey('self', models.DO_NOTHING, db_column='idTransacaoOrigem', blank=True, null=True)  # Field name made lowercase.
    statustransacao = models.CharField(db_column='statusTransacao', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datacriacao = models.DateTimeField(db_column='dataCriacao', blank=True, null=True)  # Field name made lowercase.
    dataultimaalteracao = models.DateTimeField(db_column='dataUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    datavencimento = models.DateTimeField(db_column='dataVencimento', blank=True, null=True)  # Field name made lowercase.
    valortransacao = models.DecimalField(db_column='valorTransacao', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipotransacao = models.CharField(db_column='tipoTransacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idestagiotransacao = models.ForeignKey(Estagiotransacao, models.DO_NOTHING, db_column='idEstagioTransacao', blank=True, null=True)  # Field name made lowercase.
    valordesconto = models.DecimalField(db_column='valorDesconto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codigooperacao = models.ForeignKey(Operacao, models.DO_NOTHING, db_column='codigoOperacao', blank=True, null=True)  # Field name made lowercase.
    numerotransacao = models.CharField(db_column='numeroTransacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observacaotransacao = models.CharField(db_column='observacaoTransacao', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    idcontadebito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoidContaDebito', db_column='idContaDebito', blank=True, null=True)  # Field name made lowercase.
    idcontacredito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoidContaCredito', db_column='idContaCredito', blank=True, null=True)  # Field name made lowercase.
    valorretencao = models.DecimalField(db_column='valorRetencao', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipoemissaonf = models.CharField(db_column='tipoEmissaoNF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numeronf = models.CharField(db_column='numeroNF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idcentrocusto = models.ForeignKey(Centrocusto, models.DO_NOTHING, db_column='idCentroCusto', blank=True, null=True)  # Field name made lowercase.
    pdfnota = models.CharField(db_column='pdfNota', max_length=400, blank=True, null=True)  # Field name made lowercase.
    valorpago = models.DecimalField(db_column='valorPago', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    iddup = models.ForeignKey('Transacaodup', models.DO_NOTHING, db_column='idDup', blank=True, null=True)  # Field name made lowercase.
    contasrecebergerado = models.CharField(db_column='contasReceberGerado', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacao'


class Transacaoconta(models.Model):
    idtransacaoconta = models.BigAutoField(db_column='idTransacaoConta', primary_key=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao')  # Field name made lowercase.
    idconta = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaocontaidConta', db_column='idConta')  # Field name made lowercase.
    valorlancto = models.DecimalField(db_column='valorLancto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    historicolancto = models.CharField(db_column='historicoLancto', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaoconta'


class Transacaocustomfieldvalue(models.Model):
    idcustomfieldvalue = models.BigAutoField(db_column='idCustomFieldValue', primary_key=True)  # Field name made lowercase.
    idcustomfield = models.ForeignKey(Customfield, models.DO_NOTHING, db_column='idCustomField', blank=True, null=True)  # Field name made lowercase.
    idobjeto = models.BigIntegerField(db_column='idObjeto', blank=True, null=True)  # Field name made lowercase.
    valornumericocf = models.DecimalField(db_column='valorNumericoCF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valoralfacf = models.CharField(db_column='valorAlfaCF', max_length=250, blank=True, null=True)  # Field name made lowercase.
    valordatacf = models.DateTimeField(db_column='valorDataCF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaocustomfieldvalue'


class Transacaodup(models.Model):
    iddup = models.BigAutoField(db_column='idDup', primary_key=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='dtVencto', blank=True, null=True)  # Field name made lowercase.
    dtpagto = models.DateTimeField(db_column='dtPagto', blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cobrancagerada = models.CharField(db_column='cobrancaGerada', max_length=1, blank=True, null=True)  # Field name made lowercase.
    valorcomissao = models.DecimalField(db_column='valorComissao', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dtpagtocomissao = models.DateTimeField(db_column='dtPagtoComissao', blank=True, null=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.
    tiporecebimento = models.CharField(db_column='tipoRecebimento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.CharField(db_column='numeroDocumento', max_length=150, blank=True, null=True)  # Field name made lowercase.
    chequeusado = models.CharField(db_column='chequeUsado', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaodup'


class Transacaogarantia(models.Model):
    idtransacaogarantia = models.BigAutoField(db_column='idTransacaoGarantia', primary_key=True)  # Field name made lowercase.
    relatotecnico = models.CharField(db_column='relatoTecnico', max_length=500, blank=True, null=True)  # Field name made lowercase.
    solicitacaocliente = models.CharField(db_column='solicitacaoCliente', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dtocorrencia = models.DateField(db_column='dtOcorrencia', blank=True, null=True)  # Field name made lowercase.
    dtfechamento = models.DateField(db_column='dtFechamento', blank=True, null=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaogarantia'


class Transacaoimposto(models.Model):
    idtransacaoimposto = models.BigAutoField(db_column='idTransacaoImposto', primary_key=True)  # Field name made lowercase.
    basecalculoimposto = models.DecimalField(db_column='baseCalculoImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqimposto = models.DecimalField(db_column='aliqImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valorimposto = models.DecimalField(db_column='valorImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idcontadebito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoimpostoidContaDebito', db_column='idContaDebito', blank=True, null=True)  # Field name made lowercase.
    idcontacredito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoimpostoidContaCredito', db_column='idContaCredito', blank=True, null=True)  # Field name made lowercase.
    idtipoimposto = models.ForeignKey(Tipoimposto, models.DO_NOTHING, db_column='idTipoImposto', blank=True, null=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao')  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaoimposto'


class Transacaoitem(models.Model):
    idtransacaoitem = models.BigAutoField(db_column='idTransacaoItem', primary_key=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='idProduto', blank=True, null=True)  # Field name made lowercase.
    quantidadeitem = models.DecimalField(db_column='quantidadeItem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valorunitarioitem = models.DecimalField(db_column='valorUnitarioItem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalitem = models.DecimalField(db_column='totalItem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retencaoitem = models.DecimalField(db_column='retencaoItem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descricaoitem = models.CharField(db_column='descricaoItem', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    descontoitem = models.DecimalField(db_column='descontoItem', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantidaderecebida = models.DecimalField(db_column='quantidadeRecebida', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idestoque = models.ForeignKey(Estoque, models.DO_NOTHING, db_column='idEstoque', blank=True, null=True)  # Field name made lowercase.
    quantidadefaturada = models.DecimalField(db_column='quantidadeFaturada', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtfinalgarantia = models.DateTimeField(db_column='dtFinalGarantia', blank=True, null=True)  # Field name made lowercase.
    cfopitem = models.CharField(db_column='cfopItem', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaoitem'


class Transacaoitemimposto(models.Model):
    idtransacaoitemimposto = models.BigAutoField(db_column='idTransacaoItemImposto', primary_key=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao')  # Field name made lowercase.
    idtransacaoitem = models.ForeignKey(Transacaoitem, models.DO_NOTHING, db_column='idTransacaoItem')  # Field name made lowercase.
    basecalculoimposto = models.DecimalField(db_column='baseCalculoImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqimposto = models.DecimalField(db_column='aliqImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valorimposto = models.DecimalField(db_column='valorImposto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idcontadebito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoitemimpostoidContaDebito', db_column='idContaDebito', blank=True, null=True)  # Field name made lowercase.
    idcontacredito = models.ForeignKey(Planocontas, models.DO_NOTHING, related_name='TransacaoitemimpostoidContaCredito', db_column='idContaCredito', blank=True, null=True)  # Field name made lowercase.
    idtipoimposto = models.ForeignKey(Tipoimposto, models.DO_NOTHING, db_column='idTipoImposto', blank=True, null=True)  # Field name made lowercase.
    idclifor = models.ForeignKey(Clifor, models.DO_NOTHING, db_column='idCliFor', blank=True, null=True)  # Field name made lowercase.
    cstitemimposto = models.CharField(db_column='cstItemImposto', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cfopitemimposto = models.CharField(db_column='cfopItemImposto', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaoitemimposto'


class Transacaomemorizada(models.Model):
    idtransacaomemorizacao = models.BigAutoField(db_column='idTransacaoMemorizacao', primary_key=True)  # Field name made lowercase.
    descricaomemorizacao = models.CharField(db_column='descricaoMemorizacao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    grupomemorizacao = models.CharField(db_column='grupoMemorizacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtmemorizacao = models.DateField(db_column='dtMemorizacao', blank=True, null=True)  # Field name made lowercase.
    dtultimageracao = models.DateField(db_column='dtUltimaGeracao', blank=True, null=True)  # Field name made lowercase.
    idtransacao = models.ForeignKey(Transacao, models.DO_NOTHING, db_column='idTransacao', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transacaomemorizada'
    def __str__(self):
        return '%s - %s' % (self.idtransacaomemorizacao, self.descricaomemorizacao)


class Transportadora(models.Model):
    idtransp = models.BigAutoField(db_column='idTransp', primary_key=True)  # Field name made lowercase.
    ativatransp = models.CharField(db_column='ativaTransp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    obstransp = models.CharField(db_column='obsTransp', max_length=250, blank=True, null=True)  # Field name made lowercase.
    enderecotrans = models.CharField(db_column='enderecoTrans', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cidadetrans = models.CharField(db_column='cidadeTrans', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bairrotrans = models.CharField(db_column='bairroTrans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ceptrans = models.CharField(db_column='cepTrans', max_length=8, blank=True, null=True)  # Field name made lowercase.
    numerotransp = models.CharField(db_column='numeroTransp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailtrans = models.CharField(db_column='emailTrans', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonetrans = models.CharField(db_column='telefoneTrans', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nometransp = models.CharField(db_column='nomeTransp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apelidotransp = models.CharField(db_column='apelidoTransp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    uftrans = models.ForeignKey(Estado, models.DO_NOTHING, db_column='UFTrans', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transportadora'
    def __str__(self):
        return '%s - %s' % (self.idtransp, self.nometransp)


class Transportadorascotacao(models.Model):
    idtransportadorascotacao = models.BigAutoField(db_column='idTransportadorasCotacao', primary_key=True)  # Field name made lowercase.
    idordemdespacho = models.ForeignKey(Ordemdespacho, models.DO_NOTHING, db_column='idOrdemDespacho')  # Field name made lowercase.
    idtransp = models.BigIntegerField(db_column='idTransp')  # Field name made lowercase.
    aprovada = models.CharField(max_length=1, blank=True, null=True)
    prazodias = models.DecimalField(db_column='prazoDias', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precocubado = models.DecimalField(db_column='precoCubado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pessoacontato = models.CharField(db_column='pessoaContato', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transportadorascotacao'


class Unidademedida(models.Model):
    codunimed = models.CharField(db_column='codUniMed', primary_key=True, max_length=6)  # Field name made lowercase.
    descunimed = models.CharField(db_column='descUniMed', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fatorunimed = models.DecimalField(db_column='fatorUniMed', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidademedida'
    def __str__(self):
        return self.codunimed
