from rest_framework import serializers
from .models import Curso, Avaliacao

# O Conceito de serialização é converter dados do banco
# em um tipo de dado que pode ser consumido por qualquer 
# outra linguagem Formato JSON / Objeto Javascript

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
        }
        model = Avaliacao
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'