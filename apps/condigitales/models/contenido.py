from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from apps.shared.models.linea_transversal import LineaTransversalModel
from apps.shared.models.poblacion import PoblacionModel

class ContenidoDigitalModel(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Usuario'), 
                                help_text=_('Seleccione Usuario'), on_delete=models.CASCADE,)
    
    id_linea = models.ForeignKey(LineaTransversalModel, verbose_name=_('Id linea'),
                              help_text=_('Id linea'), null=False, on_delete=models.DO_NOTHING)
     
    nombre = models.CharField(max_length=50, verbose_name=_('Nombre contenido'),
                              help_text=_('Ingresa el nombre del contenido'), null=False)
    
    url = models.CharField(max_length=50, verbose_name=_('Url contenido'),
                              help_text=_('Ingresa la url del contenido'), null=False)
    
    visibilidad = models.BooleanField(verbose_name=_('Visibilidad'), help_text=_('Selecciones la visibilidad'),
                                       null=False)
    
    OPCIONES_ESTADO = [('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')]
    estado = models.CharField(max_length=50, verbose_name=_('Estado'), help_text=_('Seleccione el estado'),
                              choices=OPCIONES_ESTADO, default=_('Pendiente'), null=False)    
    
    recomendacion = models.CharField(verbose_name=_('Recomendacion'), help_text=_('Asigne una Recomendación'),
                                      default=_('Sin recomendación'), null=True, max_length=500)

    fecha_creacion = models.DateTimeField(verbose_name=_('Fecha de Creacion'), null=False)
    
    fecha_aprobacion = models.DateTimeField(verbose_name=_('Fecha de aprobación'), null=True)

    descripcion = models.CharField(max_length=255, verbose_name=_('Descripción contenido'),
                              help_text=_('Ingresa la descripción del contenido'), null=False, default="Sin descripción")
    
    id_poblacion = models.ForeignKey(PoblacionModel, verbose_name=_('Id población'), 
                                  help_text=_('Id población'), null=False, on_delete=models.DO_NOTHING)
    
    imagen_ref = models.ImageField(verbose_name=('Imagen'),upload_to='contenidos/',  max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user}, {self.id_linea}, {self.nombre}, {self.url}, {self.visibilidad}, {self.estado}' 
        
        
    class Meta:
        verbose_name = _('Contenido digital')
        verbose_name_plural = _('Contenidos digitales')