from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
# Create your views here.

# @api_view(['GET'])
# def welcome(request):
#    return Response({"message":"Welcome to the RMS!"})

@api_view()
def category(request):
   queryset = Category.objects.all()
   serializer = CategorySerializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
   return Response(serializer.data)



# table ko endpoint: create