from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.item_acervo import ItemAcervo
from core.serializers.item_acervo import ItemAcervoSerializer

class ItemAcervoViewSet(viewsets.ModelViewSet):
    queryset = ItemAcervo.objects.all().order_by('numero_acervo')
    serializer_class = ItemAcervoSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos para filtro exato
    filterset_fields = [
        'colecao__nome',
        'materia_prima__nome',
        'subtipo_materia_prima__nome',
        'estado_conservacao',
        'localizacao_fisica__nome',
        'datacao_de',
        'datacao_ate'
    ]

    # Campos de busca textual
    search_fields = ['numero_acervo', 'titulo', 'descricao', 'observacoes']

    # Campos permitidos para ordenação
    ordering_fields = [
        'numero_acervo', 
        'titulo', 
        'datacao_de', 
        'datacao_ate', 
        'criado_em', 
        'atualizado_em'
    ]

    # Ordenação padrão
    ordering = ['numero_acervo']
