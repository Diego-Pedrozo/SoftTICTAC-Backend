from django.contrib import admin
from apps.proyectoaula.models.proyectoaula import ProyectoAulaModel
from apps.proyectoaula.models.actividad import ActividadModel

class ActividadInline(admin.StackedInline):
    model = ActividadModel  
    extra = 0

class ProyectoAulaAdmin(admin.ModelAdmin):
    inlines = [ActividadInline]
    list_display = ('id', 'user', 'id_linea', 'nombre', 'grado', 'fecha_inicio', 'fecha_fin', 'lecciones_aprendidas')

admin.site.register(ProyectoAulaModel, ProyectoAulaAdmin)