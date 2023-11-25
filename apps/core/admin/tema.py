from django.contrib import admin
from apps.shared.models.tema import TemaModel

class TemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_linea')

admin.site.register(TemaModel, TemaAdmin)