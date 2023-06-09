from django.contrib import admin

from proyecto.models import Clientes, Articulos, Pedidos, Comunicado, Categoria

# Register your models here.

class ComunicadoAdmin(admin.ModelAdmin):
    list_display=("titulo", "nivel", "fecha_envio")

"""
admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)
"""
admin.site.register(Comunicado, ComunicadoAdmin)
admin.site.register(Categoria)