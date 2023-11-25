from django.forms import ValidationError
from apps.condigitales.models.contenido import ContenidoDigitalModel
from rest_framework import serializers
from datetime import date, datetime
from apps.shared.serializers.poblacion import PoblacionSerializer
import json
from django.contrib.auth.models import User

class ContenidoDigitalSerializer(serializers.ModelSerializer):
    id_poblacion = PoblacionSerializer(many=True, read_only=True)
    archivo = serializers.FileField(required=False)
    
    class Meta:
        model = ContenidoDigitalModel
        fields = ['id', 'user', 'url', 'archivo', 'id_linea', 'nombre','descripcion', 'id_poblacion', 
                    'visibilidad', 'estado', 'recomendacion', 'fecha_creacion', 'fecha_aprobacion']
    
