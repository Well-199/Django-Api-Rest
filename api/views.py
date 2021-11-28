from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    
    def get(self, request):

        print('DIR: ', dir(request))

        print('Request Data: ', request.data)

        print('Query Params: ', request.query_params)

        print('User: ', request.user)

        # cursos recebe o nome do model e o metodo que retorna dados do banco
        cursos = Curso.objects.all()

        # serealizer recebe a o metodo que formata esse dados 
        # cursos é passado como parametro para ser formatado em JSON
        serializer = CursoSerializer(cursos, many=True)

        # serializer.data da acesso ao dados do banco em JSON 
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)


