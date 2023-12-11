from django.db import models
from django.utils.translation import gettext as _
from apps.plantrabajo.models.plantrabajo import PlanTrabajoModel

class ActividadModel(models.Model):
        
    id_plan = models.ForeignKey(PlanTrabajoModel, verbose_name=_('Id plan trabajo'),
                              help_text=_('Id plan trabajo'), null=False, on_delete=models.CASCADE,
                              related_name='actividades')
    
    nombre = models.CharField(max_length=500, verbose_name=_('Nombre de la actividad'),
                              help_text=_('Asigne un nombre a la actividad'), null=False)
    
    docentes = models.CharField(max_length=500, verbose_name=_('Docentes de apoyo'),
                              help_text=_('Asigne docentes de apoyo'), null=False)
    
    cumplimiento = models.BooleanField(verbose_name=_('Cumplimiento'), help_text=_('Cumplimiento'),
                                       null=False, default=False)

    observaciones = models.CharField(max_length=500, verbose_name=_('Observaciones'),
                              help_text=_('Asigne Observaciones'), null=True)
    
    fecha_inicio = models.DateField(verbose_name=_('Fecha de Inicio'), null=True)
    
    fecha_fin = models.DateField(verbose_name=_('Fecha de Finalización'), null=True)

    def __str__(self) -> str:
        return (f'{self.id_plan}, {self.nombre}, {self.docentes}'
                f'{self.cumplimiento}, {self.observaciones}, {self.fecha_inicio}, {self.fecha_fin}')
        
    class Meta:
        verbose_name = _('Actividad Plan de trabajo')
        verbose_name_plural = _('Actividades Plan de trabajo')