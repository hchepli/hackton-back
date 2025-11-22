from rest_framework import serializers
from core.models.movimentacao_item import MovimentacaoItem
from core.models.item_acervo import ItemAcervo
from core.models.localizacao import Localizacao
from core.models.user import User

class MovimentacaoItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=ItemAcervo.objects.all())
    localizacao_anterior = serializers.PrimaryKeyRelatedField(queryset=Localizacao.objects.all(), required=False, allow_null=True)
    localizacao_nova = serializers.PrimaryKeyRelatedField(queryset=Localizacao.objects.all(), required=False, allow_null=True)
    responsavel = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = MovimentacaoItem
        fields = [
            'id', 'tipo', 'item', 'localizacao_anterior', 'localizacao_nova',
            'motivo', 'observacoes', 'responsavel', 'data_movimentacao'
        ]
