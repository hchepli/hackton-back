from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer

class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all().order_by('nome')
    serializer_class = ColecaoSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos para filtro exato
    filterset_fields = ['coletor__nome', 'nome', 'criado_em', 'atualizado_em']

    # Campos de busca textual
    search_fields = ['nome', 'descricao', 'coletor__nome']

    # Campos permitidos para ordenação
    ordering_fields = ['nome', 'criado_em', 'atualizado_em']

    # Ordenação padrão
    ordering = ['nome']
