from django.db import models
from django.utils.translation import gettext as _
from apps.herramientas.models.momento import MomentoModel
from apps.herramientas.models.recurso import RecursoModel

class ProcesoModel(models.Model):
    id_momento = models.ForeignKey(MomentoModel, verbose_name=_('Id momento'), 
                                   help_text=_('Id momento'), on_delete=models.CASCADE,
                                   related_name='procesos')
    
    nombre = models.CharField(max_length=30, verbose_name=_('Nombre del proceso'),
                              help_text=_('Asigne un nombre al proceso'), null=False)
    
    descripcion = models.CharField(max_length=500, verbose_name=_('Descripción proceso'),
                              help_text=_('Ingresa la descripción del proceso'), null=False, default="Sin descripción")
    
    tiempo = models.IntegerField(verbose_name=_('Tiempo del proceso'), help_text=_('Ingresa el tiempo del proceso'),
                              null=False)
    
    id_recurso = models.ManyToManyField(RecursoModel, verbose_name=_('Id recurso'),
                              help_text=_('Id recurso'), related_name='procesos')

    def __str__(self) -> str:
        return f'{self.id_momento}, {self.nombre}, {self.descripcion}, {self.tiempo}, {self.id_recurso}' 
        
    class Meta:
        verbose_name = _('Proceso')
        verbose_name_plural = _('Procesos')