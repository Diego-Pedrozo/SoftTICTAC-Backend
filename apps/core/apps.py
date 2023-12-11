from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        import apps.core.admin.poblacion
        import apps.core.admin.linea_transversal
        import apps.core.admin.tema
        import apps.core.admin.competencia
        import apps.core.admin.herramienta
        #import apps.core.admin.momento
        #import apps.core.admin.recurso
        #import apps.core.admin.proceso
        import apps.core.admin.contenido
        import apps.core.admin.proyectoaula
        import apps.core.admin.plantrabajo