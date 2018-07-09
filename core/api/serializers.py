from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from enderecos.models import Endereco
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer



class PontoTuristicoSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    desc_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 
                  'aprovado', 'endereco', 'atracoes', 'comentarios', 
                  'avaliacoes', 'desc_completa', 'descricao_completa2')
        read_only_fields = ('atracoes', 'comentarios', 'avaliacoes')


    def criar_endereco(self, endereco, ponto):
        en = Endereco.objects.create(**endereco)
        ponto.endereco = en

    def criar_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        endereco = validated_data['endereco']
        atracoes = validated_data['atracoes']
        del validated_data['endereco'], validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.criar_endereco(endereco, ponto)
        self.criar_atracoes(atracoes, ponto)

        return ponto
    

    def get_desc_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
