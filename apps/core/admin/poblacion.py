from django.contrib import admin
from apps.shared.models.poblacion import PoblacionModel

class PoblacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(PoblacionModel, PoblacionAdmin)
