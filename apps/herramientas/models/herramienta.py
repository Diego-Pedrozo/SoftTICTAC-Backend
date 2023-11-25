from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from apps.shared.models.tema import TemaModel
from apps.shared.models.poblacion import PoblacionModel

class HerramientaModel(models.Model):
    
    user = models.ForeignKey(User, verbose_name=_('Usuario'), 
                                help_text=_('Seleccione Usuario'), on_delete=models.CASCADE)    

    id_tema = models.ForeignKey(TemaModel, verbose_name=_('Id tema'),
                              help_text=_('Id tema'), null=False, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=50, verbose_name=_('Nombre de la herramienta'),
                              help_text=_('Asigne un nombre a la herramienta'), null=False)
    
    objetivo = models.CharField(max_length=500, verbose_name=_('Objetivos'),
                              help_text=_('Asigne objetivos a la herramienta'), null=False)
    
    visibilidad = models.BooleanField(verbose_name=_('Visibilidad'), help_text=_('Selecciones la visibilidad'),
                                       null=False)
    
    OPCIONES_ESTADO = [('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')]
    estado = models.CharField(max_length=50, verbose_name=_('Estado'), help_text=_('Seleccione el estado'),
                              choices=OPCIONES_ESTADO, default=_('Pendiente'), null=False) 
    
    recomendacion = models.CharField(max_length=500, verbose_name=_('Recomendación'),
                              help_text=_('Asigne una Recomendación'), null=True)
    
    revision = models.CharField(verbose_name=_('Revisión'), help_text=_('Asigne una revisión'),
                                      default=_('Sin revisión'), null=True, max_length=500)
    
    fecha_creacion = models.DateTimeField(verbose_name=_('Fecha de Creacion'), null=True)
    
    fecha_aprobacion = models.DateTimeField(verbose_name=_('Fecha de aprobación'), null=True)

    id_poblacion = models.ForeignKey(PoblacionModel, verbose_name=_('Id población'), 
                                  help_text=_('Id población'), null=False, on_delete=models.DO_NOTHING)
    
    duracion = models.IntegerField(verbose_name=_('Duración de la herramienta'), null=False)

    def __str__(self) -> str:
        return ( f'{self.user}, {self.id_tema}, {self.nombre}, {self.objetivo}, {self.visibilidad}'
                f'{self.estado}, {self.recomendacion}, {self.revision}, {self.fecha_creacion}, {self.fecha_aprobacion}'
                f'{self.id_poblacion}, {self.duracion}')
        
    class Meta:
        verbose_name = _('Herramienta')
        verbose_name_plural = _('Herramientas')