from rest_framework import serializers
from .models import Category, Food

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']   # # write the field that you want to serializer
      # exclude = ['id']           # write the field that you dont want to serializer
   
   # def create(self, validated_data):
   #    return Category.objects.create(**validated_data)


class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   # category = serializers.StringRelatedField()
   # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
   category = CategorySerializer()
   class Meta:
      model = Food
      fields = ['id','name', 'price', 'price_with_tax','category']

   def get_price_with_tax(self,obj):
      return obj.price + obj.price * 0.11

   # price with 10% discount





# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       return Category.objects.create(**validated_data)
#       # return Category.objects.create(name = validated_data.get('name'))
   
#    def update(self, instance, validated_date):
#       instance.name = validated_date.get('name', instance.name)
#       instance.save()
#       return instance

# validated_data = {"name":"category1","age":50}