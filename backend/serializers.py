from rest_framework import serializers

from .models import Profesor

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesor
        fields = ('nombre', 'correo', 'celular')