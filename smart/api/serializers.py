from rest_framework import serializers
from smartapp.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'
