from django.contrib import admin
from apps.herramientas.models.momento import MomentoModel
from apps.core.admin.proceso import ProcesoInline

class MomentoInline(admin.TabularInline):
    model = MomentoModel
    extra = 0

class MomentoAdmin(admin.ModelAdmin):
    inlines = [ProcesoInline]
    list_display = ('id', 'id_herramienta', 'nombre', 'descripcion')

admin.site.register(MomentoModel, MomentoAdmin)