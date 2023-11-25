from django.contrib import admin
from apps.condigitales.models.contenido import ContenidoDigitalModel

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'archivo', 'id_linea', 'nombre', 'descripcion',
                  'visibilidad', 'estado', 'recomendacion', 'fecha_creacion', 'fecha_aprobacion')

admin.site.register(ContenidoDigitalModel, ContenidoAdmin)