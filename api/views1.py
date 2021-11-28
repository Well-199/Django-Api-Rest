from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def post(self, request):
        serializer = CursoSerializer(data=request.data)

        #metodo que verifica se os dados enviados do front são validos
        #caso não seja valido retorna ou para a execução aqui
        serializer.is_valid(raise_exception=True)

        #caso sejam validos os dados são salvo no banco
        serializer.save()

        #retorna os dados salvos e o status da requisição
        # ou pode retornar uma mensagem {"message": "success"}
        # ou Somente o ID do objeto criado | serializer.data['id']
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


