from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models.movimentacao_item import MovimentacaoItem
from core.serializers.movimentacao_item import MovimentacaoItemSerializer


# FilterSet personalizado
class MovimentacaoItemFilter(FilterSet):
    tipo = CharFilter(field_name='tipo', lookup_expr='exact')
    responsavel_email = CharFilter(field_name='responsavel__email', lookup_expr='icontains')
    item_numero_acervo = CharFilter(field_name='item__numero_acervo', lookup_expr='exact')

    class Meta:
        model = MovimentacaoItem
        fields = []


class MovimentacaoItemViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoItem.objects.all().order_by('-data_movimentacao')
    serializer_class = MovimentacaoItemSerializer

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovimentacaoItemFilter
    search_fields = ['item__titulo', 'motivo', 'observacoes']
    ordering_fields = ['data_movimentacao', 'item__numero_acervo', 'responsavel__email']
    ordering = ['-data_movimentacao']

    # CREATE customizado para debug e mensagens claras
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # retorna erros detalhados para o front
            return Response({
                "success": False,
                "errors": serializer.errors,
                "message": "Falha ao criar MovimentacaoItem"
            }, status=status.HTTP_400_BAD_REQUEST)
