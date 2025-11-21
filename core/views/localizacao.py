from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.localizacao import Localizacao
from core.serializers.localizacao import LocalizacaoSerializer

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all().order_by('nome')
    serializer_class = LocalizacaoSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos para filtro exato
    filterset_fields = ['nome', 'descricao']

    # Campos de busca textual
    search_fields = ['nome', 'descricao']

    # Campos permitidos para ordenação
    ordering_fields = ['nome', 'criado_em', 'atualizado_em']

    # Ordenação padrão
    ordering = ['nome']
