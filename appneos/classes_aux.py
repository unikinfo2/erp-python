from .models import *

def lista_menu(request):
    menus = Menu.objects.filter(modulo='Servicos').order_by("menuordem")
    menulist = {'menulista': menus}
    return menulist
