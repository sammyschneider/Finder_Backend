from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    food_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'food_detail'
    )

    class Meta:
        model = Food
        fields = "__all__"
