from apps.condigitales.models.contenido import ContenidoDigitalModel
from rest_framework import serializers
from datetime import date, datetime

class ContenidoDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidoDigitalModel
        fields = ['user','id_linea', 'id', 'nombre', 'url', 'visibilidad', 'estado',
                   'recomendacion', 'fecha_creacion', 'fecha_aprobacion',
                   'descripcion', 'id_poblacion', 'imagen_ref']