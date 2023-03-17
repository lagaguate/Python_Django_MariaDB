from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono","email")
    search_fields=("nombre","telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    search_fields=("nombre","seccion")
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")    
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
