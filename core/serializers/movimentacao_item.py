from rest_framework import serializers
from core.models.movimentacao_item import MovimentacaoItem
from core.models.item_acervo import ItemAcervo
from core.models.localizacao import Localizacao
from core.models.user import User
from core.serializers.item_acervo import ItemAcervoSerializer
from core.serializers.localizacao import LocalizacaoSerializer
from core.serializers.user import UserSerializer

class MovimentacaoItemSerializer(serializers.ModelSerializer):
    item = ItemAcervoSerializer(read_only=True)
    localizacao_anterior = LocalizacaoSerializer(read_only=True)
    localizacao_nova = LocalizacaoSerializer(read_only=True)
    responsavel = UserSerializer(read_only=True)

    class Meta:
        model = MovimentacaoItem
        fields = [
            'id', 'tipo', 'item', 'localizacao_anterior', 'localizacao_nova',
            'motivo', 'observacoes', 'responsavel', 'data_movimentacao'
        ]

