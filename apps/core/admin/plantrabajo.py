from django.contrib import admin
from apps.plantrabajo.models.plantrabajo import PlanTrabajoModel
from apps.plantrabajo.models.actividad import ActividadModel

class ActividadInline(admin.StackedInline):
    model = ActividadModel  
    extra = 0

class PlanTrabajoAdmin(admin.ModelAdmin):
    inlines = [ActividadInline]
    list_display = ('id', 'user', 'id_linea', 'nombre', 'año', 'lecciones_aprendidas')

admin.site.register(PlanTrabajoModel, PlanTrabajoAdmin)