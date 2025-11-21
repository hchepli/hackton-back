from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.subtipo_materia_prima import SubtipoMateriaPrima
from core.serializers.subtipo_materia_prima import SubtipoMateriaPrimaSerializer

class SubtipoMateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = SubtipoMateriaPrima.objects.all().order_by('nome')
    serializer_class = SubtipoMateriaPrimaSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos para filtro exato
    filterset_fields = ['materia_prima__nome']

    # Campos de busca textual
    search_fields = ['nome']

    # Campos permitidos para ordenação
    ordering_fields = ['nome', 'materia_prima__nome']

    # Ordenação padrão
    ordering = ['nome']
