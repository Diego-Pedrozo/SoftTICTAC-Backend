from django.db import models
from django.utils.translation import gettext as _

class UserRanges(models.TextChoices):
    Administrativo = 1,_('Administrativo')
    LiderPPT = 2, _('Lider PPT')
    Docente = 3, _('Docente')

