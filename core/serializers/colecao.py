from rest_framework import serializers
from core.models import Colecao, Coletor

class ColecaoSerializer(serializers.ModelSerializer):
    # Agora retorna o objeto completo do coletor (read-only para GET)
    coletor = serializers.SerializerMethodField()
    coletor_id = serializers.PrimaryKeyRelatedField(
        queryset=Coletor.objects.all(), write_only=True, source='coletor'
    )

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'coletor', 'coletor_id', 'criado_em', 'atualizado_em']

    def get_coletor(self, obj):
        if obj.coletor:
            return {
                "id": obj.coletor.id,
                "nome": obj.coletor.nome,
                "biografia": obj.coletor.biografia
            }
        return None
