from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from core.models.auditoria import Auditoria
from core.serializers.auditoria import AuditoriaSerializer

class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auditoria.objects.all().order_by('-data')
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAdminUser]

    # Adicionando filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Campos para filtro exato (FK, escolha, texto)
    filterset_fields = ['usuario__email', 'acao', 'modelo', 'data']
    
    # Campos de busca textual (conteúdo)
    search_fields = ['descricao', 'modelo', 'usuario__email']
    
    # Campos permitidos para ordenação
    ordering_fields = ['data', 'usuario__email', 'acao', 'modelo']
    
    # Ordenação padrão
    ordering = ['-data']
