from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']   # # write the field that you want to serializer
      # exclude = ['id']           # write the field that you dont want to serializer
   
   # def create(self, validated_data):
   #    return Category.objects.create(**validated_data)


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