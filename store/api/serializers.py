# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from store.models import Product


class ProductSerializers(serializers.ModelSerializer):
    image_url = serializers.StringRelatedField(source="image")
    class Meta:
        model = Product
        fields = ["name", "price", "image_url"]