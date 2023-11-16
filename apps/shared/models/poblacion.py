from django.db import models
from django.utils.translation import gettext as _

class PoblacionModel(models.Model):
    
    nombre = models.CharField(max_length=30, verbose_name=_('Nombre de población'),
                              help_text=_('Asigne un nombre a la población'), null=False,)

    def __str__(self) -> str:
        return f'{self.nombre}' 
        
    class Meta:
        verbose_name = _('Población')
        verbose_name_plural = _('Poblaciones')