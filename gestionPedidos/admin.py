from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
