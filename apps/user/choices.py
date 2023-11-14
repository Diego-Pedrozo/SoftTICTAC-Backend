from django.db import models
from django.utils.translation import gettext as _

class  UserRanges(models.TextChoices):
    ADMIN = 1,_('Administrador')
    CLIENT = 2, _('Cliente')