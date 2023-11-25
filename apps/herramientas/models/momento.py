from django.db import models
from django.utils.translation import gettext as _
from apps.herramientas.models.herramienta import HerramientaModel

class MomentoModel(models.Model):
    
    id_herramienta = models.ForeignKey(HerramientaModel, verbose_name=_('Id herramienta'), 
                                       help_text=_('Id herramienta'), on_delete=models.CASCADE,
                                       related_name='momentos')
    
    nombre = models.CharField(max_length=30, verbose_name=_('Nombre del momento'),
                              help_text=_('Asigne un nombre al momento'), null=False)
    
    descripcion = models.CharField(max_length=500, verbose_name=_('Descripción momento'),
                              help_text=_('Ingresa la descripción del momento'), null=False, default="Sin descripción")
    
    def __str__(self) -> str:
        return f'{self.id_herramienta}, {self.nombre}, {self.descripcion}' 
        
    class Meta:
        verbose_name = _('Momento')
        verbose_name_plural = _('Momentos')