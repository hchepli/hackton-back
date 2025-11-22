from rest_framework.viewsets import ModelViewSet
from core.models.user import User
from core.serializers.user import (
    UserSerializer,
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    search_fields = ["name", "email"]
    filterset_fields = ["perfil"]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        if self.action in ["update", "partial_update"]:
            return UserUpdateSerializer
        if self.action == "list":
            return UserListSerializer
        return UserSerializer

    # -----------------------------
    # Remove todas as permissões
    # -----------------------------
    def get_permissions(self):
        return []  # sem restrição nenhuma

    # -----------------------------
    # Métodos customizados
    # -----------------------------
    def perform_create(self, serializer):
        # Define perfil padrão como 'usuario' se não for informado
        perfil = serializer.validated_data.get('perfil', 'usuario')
        serializer.save(perfil=perfil)

    def perform_update(self, serializer):
        # Atualiza normalmente, sem restrição
        serializer.save()

    def me(self, request):
        # Retorna dados do próprio usuário, mas sem permissão
        return Response(UserSerializer(request.user).data)
