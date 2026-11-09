from django.contrib import admin
from .models import Categoria, Material

admin.site.site_header = ("ConstruStock - Panel de Control")
admin.site.site_title = ("ConstruStock Admin")
admin.site.index_title = ("Gestión de Materiales")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombre_categoria"
    )

    search_fields = (
        "nombre_categoria",
    )

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "categoria",
        "precio_referencia",
        "activo"
    )
    search_fields = (
        "codigo",
        "nombre"
    )

    list_filter = (
        "categoria",
        "activo"
)