from django.contrib import admin
from apps.herramientas.models.proceso import ProcesoModel

class ProcesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_momento', 'nombre', 'descripcion', 'tiempo')

admin.site.register(ProcesoModel, ProcesoAdmin)