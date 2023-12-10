from django.contrib import admin
from apps.herramientas.models.proceso import ProcesoModel

class ProcesoInline(admin.TabularInline):
    model = ProcesoModel
    extra = 0

class ProcesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_momento', 'descripcion', 'tiempo')

admin.site.register(ProcesoModel, ProcesoAdmin)