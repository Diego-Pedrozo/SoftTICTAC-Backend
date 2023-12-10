from django.contrib import admin
from apps.herramientas.models.herramienta import HerramientaModel
from apps.core.admin.momento import MomentoInline

class HerramientaAdmin(admin.ModelAdmin):
    inlines = [MomentoInline]
    list_display = ('id', 'user', 'id_tema', 'nombre', 'objetivo', 'visibilidad', 'estado', 
                    'recomendacion', 'revision', 'fecha_creacion', 'fecha_aprobacion', 'duracion')

admin.site.register(HerramientaModel, HerramientaAdmin)