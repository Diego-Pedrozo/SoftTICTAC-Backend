from django.db import models
from django.utils.translation import gettext as _

class RecursoModel(models.Model):

    # id_proceso = models.ForeignKey(ProcesoModel, verbose_name=_('Id proceso'),
    #                           help_text=_('Id proceso'), null=False, on_delete=models.DO_NOTHING)

    # nombre = models.CharField(max_length=50, verbose_name=_('Nombre del recurso'),
    #                           help_text=_('Asigne un nombre al recurso'), null=False)
    
    # url = models.CharField(max_length=100, verbose_name=_('Url'),
    #                           help_text=_('Asigne una Url'), null=True)
    tipo = models.CharField(max_length=100, verbose_name=_('Tipo de recurso'),
                              help_text=_('Seleccione un tipo de recurso'), null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.tipo}' 
        
    class Meta:
        verbose_name = _('Recurso')
        verbose_name_plural = _('Recursos')