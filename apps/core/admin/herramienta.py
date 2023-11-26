from django.contrib import admin
from apps.herramientas.models.herramienta import HerramientaModel

class HerramientaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'id_tema', 'nombre', 'objetivo', 'visibilidad', 'estado', 
                    'recomendacion', 'revision', 'fecha_creacion', 'fecha_aprobacion', 'duracion')

admin.site.register(HerramientaModel, HerramientaAdmin)