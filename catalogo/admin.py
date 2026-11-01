from django.contrib import admin
from .models import Categoria, Material

admin.site.site_header = "Sistema de Materiales - Panel de Control"
admin.site.site_title = "Sistema Materiales"
admin.site.index_title = "Gestión de Materiales"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria')
    search_fields = ('nombre_categoria',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'stock',
        'precio_referencia',
        'categoria'
    )

    search_fields = (
        'nombre',
        'descripcion'
    )

    list_filter = (
        'categoria',
    )