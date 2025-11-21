from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.movimentacao_item import MovimentacaoItem
from core.serializers.movimentacao_item import MovimentacaoItemSerializer

class MovimentacaoItemViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoItem.objects.all().order_by('-data_movimentacao')
    serializer_class = MovimentacaoItemSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos para filtro exato
    filterset_fields = ['item__numero_acervo', 'tipo_movimentacao', 'usuario__email']

    # Campos de busca textual
    search_fields = ['item__titulo', 'descricao']

    # Campos permitidos para ordenação
    ordering_fields = ['data_movimentacao', 'item__numero_acervo', 'usuario__email']

    # Ordenação padrão
    ordering = ['-data_movimentacao']
