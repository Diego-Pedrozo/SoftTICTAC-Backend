from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from apps.shared.models.linea_transversal import LineaTransversalModel

class PlanTrabajoModel(models.Model):
    
    user = models.ForeignKey(User, verbose_name=_('Usuario'), 
                                help_text=_('Seleccione Usuario'), on_delete=models.CASCADE) 
    
    id_linea = models.ForeignKey(LineaTransversalModel, verbose_name=_('Id linea'),
                              help_text=_('Id linea'), null=False, on_delete=models.DO_NOTHING)
    
    nombre = models.CharField(max_length=500, verbose_name=_('Nombre del proyecto de aula'),
                              help_text=_('Asigne un nombre al proyecto de aula'), null=False)
    
    año = models.IntegerField(verbose_name=_('Fecha de Inicio'), null=True)
    
    lecciones_aprendidas = models.CharField(max_length=500, verbose_name=_('Lecciones Aprendidas'),
                              help_text=_('Asigne las Lecciones Aprendidas'), null=True)

    def __str__(self) -> str:
        return (f'{self.user}, {self.id_linea}, {self.nombre}'
                f'{self.año}, {self.lecciones_aprendidas}')
        
    class Meta:
        verbose_name = _('Plan de trabajo')
        verbose_name_plural = _('Planes de trabajo')