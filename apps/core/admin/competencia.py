from django.contrib import admin
from apps.shared.models.competencia import CompetenciaModel

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(CompetenciaModel, CompetenciaAdmin)