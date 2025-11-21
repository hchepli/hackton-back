from rest_framework import viewsets, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from core.models.imagem_item import ImagemItem
from core.serializers.imagem_item import ImagemItemSerializer

class ImagemItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar imagens de itens do acervo.
    Suporta:
      - listagem com filtros por item
      - busca textual por legenda
      - ordenação por data de criação
      - upload de múltiplas imagens via POST
    """
    queryset = ImagemItem.objects.all().order_by('-criado_em')
    serializer_class = ImagemItemSerializer
    permission_classes = [AllowAny]

    # Filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['item__numero_acervo', 'item__titulo']  # filtro por item
    search_fields = ['legenda']  # busca textual
    ordering_fields = ['criado_em', 'id']
    ordering = ['-criado_em']

    def create(self, request, *args, **kwargs):
        """
        Permite criar múltiplas imagens em um único POST.
        Espera:
          - 'item': ID do ItemAcervo
          - 'imagem': um arquivo de imagem (ou múltiplos arquivos via FormData)
        """
        item_id = request.data.get('item')
        files = request.FILES.getlist('imagem')

        if not item_id:
            return Response({'item': 'Campo obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

        if not files:
            return Response({'imagem': 'Ao menos um arquivo deve ser enviado'}, status=status.HTTP_400_BAD_REQUEST)

        created = []
        for f in files:
            serializer = self.get_serializer(data={'item': item_id, 'imagem': f})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created.append(serializer.data)

        return Response(created, status=status.HTTP_201_CREATED)
