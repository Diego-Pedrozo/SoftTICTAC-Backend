from django.contrib import admin
from apps.shared.models.linea_transversal import LineaTransversalModel

class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(LineaTransversalModel, LineaAdmin)