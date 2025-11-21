from rest_framework import serializers
from core.models.imagem_item import ImagemItem
from core.models.item_acervo import ItemAcervo

class ImagemItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(
        queryset=ItemAcervo.objects.all()
    )

    class Meta:
        model = ImagemItem
        fields = '__all__'
