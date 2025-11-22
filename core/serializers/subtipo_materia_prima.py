from rest_framework import serializers
from core.models.subtipo_materia_prima import SubtipoMateriaPrima
from core.models.materia_prima import MateriaPrima

class SubtipoMateriaPrimaSerializer(serializers.ModelSerializer):
    materia_prima = serializers.PrimaryKeyRelatedField(
        queryset=MateriaPrima.objects.all()
    )

    class Meta:
        model = SubtipoMateriaPrima
        fields = '__all__'
