from django.db import models
from django.utils.translation import gettext as _

class LineaTransversalModel(models.Model):
    
    nombre = models.CharField(max_length=100, verbose_name=_('Nombre de linea transversal'),
                              help_text=_('Asigne un nombre a la linea transversal'), null=False,
                              unique=True, error_messages={'unique': 'Ya existe una linea transversal con este nombre.'})

    def __str__(self) -> str:
        return f'{self.nombre}' 
        
    class Meta:
        verbose_name = _('Linea transversal')
        verbose_name_plural = _('Lineas transversales')