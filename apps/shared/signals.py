from django.utils.translation import gettext as _
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from apps.shared.models.poblacion import PoblacionModel
from apps.shared.models.linea_transversal import LineaTransversalModel
from apps.shared.models.competencia import CompetenciaModel

@receiver(post_migrate)
def created_static_tables(sender, **kwargs):
    poblaciones_db = PoblacionModel.objects
    poblacion_primaria= {
                'nombre': 'Basica Primaria',
                }
    poblacion_secundaria= {
                'nombre': 'Basica Secundaria',
                }
    poblacion_media= {
                'nombre': 'Media',
                }
    
    if not poblaciones_db.filter(nombre=poblacion_primaria['nombre']).exists():
        poblaciones_db.get_or_create(**poblacion_primaria)
    
    if not poblaciones_db.filter(nombre=poblacion_secundaria['nombre']).exists():
        poblaciones_db.get_or_create(**poblacion_secundaria)
    
    if not poblaciones_db.filter(nombre=poblacion_media['nombre']).exists():
        poblaciones_db.get_or_create(**poblacion_media)

    ########################################################
    lineas_db = LineaTransversalModel.objects
    linea_1= {'nombre': 'Emprendimiento'}
    linea_2= {'nombre': 'Sexualidad'}
    linea_3= {'nombre': 'Relaciones Sociales'}
    linea_4= {'nombre': 'Medio Ambiente'}
    linea_5= {'nombre': 'TICS'}
    
    if not poblaciones_db.filter(nombre=linea_1['nombre']).exists():
        lineas_db.get_or_create(**linea_1)
    
    if not poblaciones_db.filter(nombre=linea_2['nombre']).exists():
        lineas_db.get_or_create(**linea_2)
    
    if not poblaciones_db.filter(nombre=linea_3['nombre']).exists():
        lineas_db.get_or_create(**linea_3)

    if not poblaciones_db.filter(nombre=linea_4['nombre']).exists():
        lineas_db.get_or_create(**linea_4)
    
    if not poblaciones_db.filter(nombre=linea_5['nombre']).exists():
        lineas_db.get_or_create(**linea_5)

    ########################################################
    competencias_db = CompetenciaModel.objects
    competencia_1= {'nombre': ' Participa activamente en los ámbitos sociales e interpersonales, manifestando solidaridad e interés por la comunidad.'}
    competencia_2= {'nombre': 'Capacidad de comunicarse constructivamente.'}
    competencia_3= {'nombre': 'Conoce y aplica las normas de tránsito y seguridad vial.'}
    competencia_4= {'nombre': 'Comprende los aspectos de la sexualidad humana, sus transiciones e implicaciones en la vida cotidiana.'}
    competencia_5= {'nombre': 'Identifica la diversidad que existe en los seres humanos y sus formas de expresarla.'}
    competencia_6= {'nombre': 'Toma decisiones centradas en el enfoque de derechos sexuales y reproductivos.'}
    competencia_7= {'nombre': 'Comprende los procesos de cuidado y protección del medio ambiente.'}
    competencia_8= {'nombre': 'Cuida y protege el medio ambiente.'}
    competencia_9= {'nombre': 'Promueve en su comunidad el cuidado y protección del medio ambiente.'}
    competencia_10= {'nombre': 'Desarrolla pensamiento emprendedor en el ser, sentir, pensar y actuar.'}
    competencia_11= {'nombre': 'Desarrolla hábitos y valores emprendedores que orienten el comportamiento para el éxito personal.'}
    competencia_12= {'nombre': 'Tiene capacidad para entender el entorno socioeconómico en su contexto.'}
    competencia_13= {'nombre': 'Comprende que las TIC facilitan responder a problemas de su entorno y se deben utilizar de manera responsable.'}
    competencia_14= {'nombre': 'Integra las TIC en el desarrollo de las actividades académicas y cotidianas para facilitar y agilizar los procesos operativos en los diferentes contextos.'}
    competencia_15= {'nombre': 'Construye soluciones a problemas del contexto usando las TIC.'}
    
    if not competencias_db.filter(nombre=competencia_1['nombre']):
        competencias_db.get_or_create(**competencia_1)
    
    if not competencias_db.filter(nombre=competencia_2['nombre']):
        competencias_db.get_or_create(**competencia_2)
    
    if not competencias_db.filter(nombre=competencia_3['nombre']):
        competencias_db.get_or_create(**competencia_3)

    if not competencias_db.filter(nombre=competencia_4['nombre']):
        competencias_db.get_or_create(**competencia_4)
    
    if not competencias_db.filter(nombre=competencia_5['nombre']):
        competencias_db.get_or_create(**competencia_5)

    if not competencias_db.filter(nombre=competencia_6['nombre']):
        competencias_db.get_or_create(**competencia_6)
    
    if not competencias_db.filter(nombre=competencia_7['nombre']):
        competencias_db.get_or_create(**competencia_7)
    
    if not competencias_db.filter(nombre=competencia_8['nombre']):
        competencias_db.get_or_create(**competencia_8)

    if not competencias_db.filter(nombre=competencia_9['nombre']):
        competencias_db.get_or_create(**competencia_9)
    
    if not competencias_db.filter(nombre=competencia_10['nombre']):
        competencias_db.get_or_create(**competencia_10)

    if not competencias_db.filter(nombre=competencia_11['nombre']):
        competencias_db.get_or_create(**competencia_11)
    
    if not competencias_db.filter(nombre=competencia_12['nombre']):
        competencias_db.get_or_create(**competencia_12)
    
    if not competencias_db.filter(nombre=competencia_13['nombre']):
        competencias_db.get_or_create(**competencia_13)

    if not competencias_db.filter(nombre=competencia_14['nombre']):
        competencias_db.get_or_create(**competencia_14)
    
    if not competencias_db.filter(nombre=competencia_15['nombre']):
        competencias_db.get_or_create(**competencia_15)

    


    