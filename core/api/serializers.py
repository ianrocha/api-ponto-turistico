from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIdentificacao
from enderecos.models import Endereco
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    doc_identificacao = DocIdentificacaoSerializer()
    desc_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 
                  'aprovado', 'endereco', 'atracoes', 'comentarios', 
                  'avaliacoes', 'desc_completa', 'descricao_completa2',
                  'doc_identificacao')
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
        del validated_data['endereco']

        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        
        self.criar_endereco(endereco, ponto)
        self.criar_atracoes(atracoes, ponto)
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto
    

    def get_desc_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
