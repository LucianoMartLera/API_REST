from rest_framework import serializers

from examen.models import Proyecto

class ProyectSerializar(serializers.ModelSerializer):
    class Meta:
        model=Proyecto
        fields="__all__"
