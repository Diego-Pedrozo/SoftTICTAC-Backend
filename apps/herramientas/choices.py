from django.db import models
from django.utils.translation import gettext as _

class TiposRecurso(models.TextChoices):
    Video = 1,_('Video')
    Imagen = 2,_('Imagen')
    Proyector = 3,_('Proyector')
    Sonido = 4,_('Sonido')
    Computador = 5,_('Computador')