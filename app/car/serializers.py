from rest_framework import serializers
from app.car.models import Car, Category  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  

class CarSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) 
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True  
    )

    class Meta:
        model = Car
        fields = "__all__"
