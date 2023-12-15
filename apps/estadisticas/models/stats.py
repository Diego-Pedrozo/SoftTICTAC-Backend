from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class UserStatsModel(models.Model):
    user = models.OneToOneField(User, 
                                 on_delete=models.CASCADE, 
                                 verbose_name=_('Usuario'), 
                                 help_text=_('Seleccione Usuario'),
                                 related_name='stats', 
                                 null=True)
    
    proyectos_emprendimiento = models.IntegerField(default = 0, verbose_name=_('Proyectos de emprendimiento'), null=True)
    proyectos_sexualidad = models.IntegerField(default = 0, verbose_name=_('Proyectos de sexualidad'), null=True)
    proyectos_relaciones_sociales = models.IntegerField(default = 0, verbose_name=_('Proyectos de relaciones sociales'), null=True)
    proyectos_medio_ambiente = models.IntegerField(default = 0, verbose_name=_('Proyectos de medio ambiente'), null=True)
    proyectos_tics = models.IntegerField(default = 0, verbose_name=_('Proyectos de tics'), null=True)

    contenidos_emprendimiento = models.IntegerField(default = 0, verbose_name=_('Contenidos de emprendimiento'), null=True)
    contenidos_sexualidad = models.IntegerField(default = 0, verbose_name=_('Contenidos de sexualidad'), null=True)
    contenidos_relaciones_sociales = models.IntegerField(default = 0, verbose_name=_('Contenidos de relaciones sociales'), null=True)
    contenidos_medio_ambiente = models.IntegerField(default = 0, verbose_name=_('Contenidos de medio ambiente'), null=True)
    contenidos_tics = models.IntegerField(default = 0, verbose_name=_('Contenidos de tics'), null=True)

    herramientas_emprendimiento = models.IntegerField(default = 0, verbose_name=_('Herramientas de emprendimiento'), null=True)
    herramientas_sexualidad = models.IntegerField(default = 0, verbose_name=_('Herramientas de sexualidad'), null=True)
    herramientas_relaciones_sociales = models.IntegerField(default = 0, verbose_name=_('Herramientas de relaciones sociales'), null=True)
    herramientas_medio_ambiente = models.IntegerField(default = 0, verbose_name=_('Herramientas de medio ambiente'), null=True)
    herramientas_tics = models.IntegerField(default = 0, verbose_name=_('Herramientas de tics'), null=True)
    
    def __str__(self) -> str:
        return (
            f'{self.user}, {self.proyectos_emprendimiento}, {self.proyectos_sexualidad}, {self.proyectos_relaciones_sociales}, {self.proyectos_medio_ambiente}, {self.proyectos_tics}'
            f'{self.contenidos_emprendimiento}, {self.contenidos_sexualidad}, {self.contenidos_relaciones_sociales}, {self.contenidos_medio_ambiente}, {self.contenidos_tics}'
            f'{self.herramientas_emprendimiento}, {self.herramientas_sexualidad}, {self.herramientas_relaciones_sociales}, {self.herramientas_medio_ambiente}, {self.herramientas_tics}'
        )
    
    class Meta:
        verbose_name = _('Estadistica')
        verbose_name_plural = _('Estadisticas')
