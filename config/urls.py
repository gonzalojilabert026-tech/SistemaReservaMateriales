from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.urls')),
    path('catalogo/', include('apps.catalogo.urls')),
]

# Servir archivos multimedia durante el desarrollo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)