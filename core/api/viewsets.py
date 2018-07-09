from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
# from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from django.http import HttpResponse


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome','endereco__linha1',)
    # permission_classes = (DjangoModelPermissions,)
    # authentication_classes = (TokenAuthentication,)
    # Muda argumento padrão de pesquisa
    # lookup_field = 'nome'


    def get_queryset(self):
        # Exemplo de filtro com query-string
        # id = self.request.query_params.get('id', None)
        # nome = self.request.query_params.get('nome', None)
        # descricao = self.request.query_params.get('descricao', None)
        # queryset = PontoTuristico.objects.all()

        # if id:
        #     queryset = queryset.objects.filter(pk=id)

        # if nome:
        #     queryset = queryset.objects.filter(nome__iexact=nome)

        # if descricao:
        #     queryset = queryset.objects.filter(descricao__iexact=descricao)

        # return queryset
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)

        for atracao in atracoes:
            ponto.atracoes.add(atracao)
        
        ponto.save()

        return HttpResponse('Ok')