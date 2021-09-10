from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import *


@login_required
def empresa_listar(request, template_name="empresa/empresa_list.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get('page', '')
    ordem = request.GET.get("ordenar", '')
    empresa = Empresa.objects.all()

    if ordem:
        if ordem != '':
            ordenar = ordem
    try:
        if ordem == '':
            ordenar = 'razaoemp'
        if ordem == 'todos':
            ordenar = 'razaoemp'
    except:
      ordenar = 'razaoemp'

    try:
        if query:
            if ordenar == 'idempresa':
                empresa = Empresa.objects.filter(idempresa__icontains=query).order_by(ordenar)
            else:
                if ordenar == 'cnpjemp':
                    empresa = Empresa.objects.filter(cnpjemp__icontains=query).order_by(ordenar)
                else:
                    if ordenar == 'razaoemp':
                        empresa = Empresa.objects.filter(razaoemp__icontains=query).order_by(ordenar)
                    else:
                        if ordenar == 'emailemp':
                            empresa = Empresa.objects.filter(emailemp__icontains=query).order_by(ordenar)
                        else:
                            empresa = Empresa.objects.all().order_by('razaoemp')
        else:
            empresa = Empresa.objects.all().order_by(ordenar)

        empresa = Paginator(empresa, 10)
        empresa = empresa.page(page)
    except PageNotAnInteger:
        empresa = empresa.page(1)
    except EmptyPage:
        empresa = paginator.page(paginator.num_pages)

    empresas = {'lista': empresa}
    return render(request, template_name, empresas)

@login_required
def empresa_perfil(request, id, template_name="empresa/empresa_perfil.html"):
    empresa = get_object_or_404(Empresa, pk=id)
    return render(request, template_name, {'empresa': empresa})

