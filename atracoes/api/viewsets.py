from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
# Import para filtro
from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # Filtro backend utilizado
    filter_backends = (DjangoFilterBackend,)
    # Campos que podem ser filtrados
    filter_fields = ('nome', 'descricao')