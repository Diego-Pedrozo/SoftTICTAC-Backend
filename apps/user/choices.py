from django.db import models
from django.utils.translation import gettext as _

class UserRanges(models.TextChoices):
    Administrativo = 0,_('Administrativo')
    LiderEmprendimiento = 1, _('Lider Emprendimiento')
    LiderSexualidad = 2, _('Lider Sexualidad')
    LiderRelacionesSociales = 3, _('Lider Relaciones Sociales')
    LiderMedioAmbiente = 4, _('Lider Medio Ambiente')
    LiderTICS = 5, _('Lider TICS')
    Docente = 6, _('Docente')

