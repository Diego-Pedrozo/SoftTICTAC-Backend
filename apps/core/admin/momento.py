from django.contrib import admin
from apps.herramientas.models.momento import MomentoModel

class MomentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_herramienta', 'nombre', 'descripcion')

admin.site.register(MomentoModel, MomentoAdmin)