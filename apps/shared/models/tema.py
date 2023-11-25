from django.db import models
from django.utils.translation import gettext as _
from apps.shared.models.competencia import CompetenciaModel
from apps.shared.models.linea_transversal import LineaTransversalModel

class TemaModel(models.Model):
    
    nombre = models.CharField(max_length=500, verbose_name=_('Nombre del tema'),
                              help_text=_('Asigne un nombre al tema'), null=False)
    
    id_linea = models.ForeignKey(LineaTransversalModel, verbose_name=_('Id linea'),
                              help_text=_('Id linea'), null=False, on_delete=models.DO_NOTHING)
    
    id_competencia = models.ManyToManyField(CompetenciaModel, verbose_name=_('Id competencia'),
                              help_text=_('Id competencia'), related_name='temas')

    def __str__(self) -> str:
        return f'{self.nombre}, {self.id_linea}, {self.id_competencia}' 
        
    class Meta:
        verbose_name = _('Tema')
        verbose_name_plural = _('Temas')