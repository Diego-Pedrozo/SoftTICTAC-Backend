from django.contrib import admin
from apps.herramientas.models.recurso import RecursoModel

class RecursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')

admin.site.register(RecursoModel, RecursoAdmin)