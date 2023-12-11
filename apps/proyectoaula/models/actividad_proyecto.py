from django.db import models
from django.utils.translation import gettext as _
from apps.proyectoaula.models.proyectoaula import ProyectoAulaModel

class ActividadProyectoModel(models.Model):
        
    id_proyectoaula = models.ForeignKey(ProyectoAulaModel, verbose_name=_('Id proyecto aula'),
                              help_text=_('Id proyecto aula'), null=False, on_delete=models.CASCADE,
                              related_name='actividades')
    
    nombre = models.CharField(max_length=500, verbose_name=_('Nombre del proyecto de aula'),
                              help_text=_('Asigne un nombre al proyecto de aula'), null=False)
    
    descripcion = models.CharField(max_length=50, verbose_name=_('Descripción'),
                              help_text=_('Asigne una descripción'), null=False)
    
    estudiantes = models.CharField(max_length=500, verbose_name=_('Estudiantes de apoyo'),
                              help_text=_('Asigne estudiantes de apoyo'), null=False)
    
    cumplimiento = models.BooleanField(verbose_name=_('Cumplimiento'), help_text=_('Cumplimiento'),
                                       null=False, default=False)

    observaciones = models.CharField(max_length=500, verbose_name=_('Observaciones'),
                              help_text=_('Asigne Observaciones'), null=True)
    
    fecha_inicio = models.DateField(verbose_name=_('Fecha de Inicio'), null=True)
    
    fecha_fin = models.DateField(verbose_name=_('Fecha de Finalización'), null=True)

    def __str__(self) -> str:
        return (f'{self.id_proyectoaula}, {self.nombre}, {self.descripcion}, {self.estudiantes}'
                f'{self.cumplimiento}, {self.observaciones}, {self.fecha_inicio}, {self.fecha_fin}')
        
    class Meta:
        verbose_name = _('Actividad Proyecto de aula')
        verbose_name_plural = _('Actividades Proyecto de aula')