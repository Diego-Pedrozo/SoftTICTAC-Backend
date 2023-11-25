from django.db import models
from django.utils.translation import gettext as _

class CompetenciaModel(models.Model):
    
    nombre = models.CharField(max_length=500, verbose_name=_('Nombre de la competencia'),
                              help_text=_('Asigne un nombre a la competencia'), null=False)

    def __str__(self) -> str:
        return f'{self.nombre}' 
        
    class Meta:
        verbose_name = _('Competencia')
        verbose_name_plural = _('Competencias')