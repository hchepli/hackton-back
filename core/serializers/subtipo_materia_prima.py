from rest_framework import serializers
from core.models.subtipo_materia_prima import SubtipoMateriaPrima
from core.models.materia_prima import MateriaPrima
from core.serializers.materia_prima import MateriaPrimaSerializer

class SubtipoMateriaPrimaSerializer(serializers.ModelSerializer):
    materia_prima = MateriaPrimaSerializer(read_only=True)  # Inclui o objeto completo
    materia_prima_id = serializers.PrimaryKeyRelatedField(queryset=MateriaPrima.objects.all(), write_only=True)  # para POST

    class Meta:
        model = SubtipoMateriaPrima
        fields = '__all__'

