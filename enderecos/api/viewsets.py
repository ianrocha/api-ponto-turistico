from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer
# from rest_framework.permissions import IsAdminUser
# from rest_framework.authentication import TokenAuthentication

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    # permission_classes = (IsAdminUser,)
    # authentication_classes = (TokenAuthentication,)