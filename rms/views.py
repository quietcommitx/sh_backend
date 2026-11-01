from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import CategorySerializer, FoodSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.

# class based 
# modelviewset
from rest_framework.viewsets import ModelViewSet
from .pagination import CategoryPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FoodFilter
class CategoryModelViewSet(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   pagination_class = CategoryPagination
   permission_classes = [IsAuthenticatedOrReadOnly]



class FoodModelViewSet(ModelViewSet):
   queryset = Food.objects.all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   filter_backends = [filters.SearchFilter, DjangoFilterBackend]
   search_fields = ['name']
   # filterset_fields = ['category__name','price']
   filterset_class = FoodFilter
   permission_classes = [IsAuthenticated]









# Viewset
# from rest_framework import viewsets
# class CategoryViewSet(viewsets.ViewSet):
#    def list(self, request):
#       queryset = Category.objects.all()
#       serializer = CategorySerializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
#       return Response(serializer.data)
   
#    def create(self, request):
#       serializer = CategorySerializer(data = request.data)   # deserialization: covent json into model instance
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# class CategoryDetailGenericAPIView(viewsets.ViewSet):
#    def retrieve(self, request, pk):
#       queryset = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
#       return Response(serializer.data)
   
#    def update(self, request,pk):
#       queryset = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(queryset, data=request.data, partial=True)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def partial_update(self, request, pk=None):
#       queryset = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(queryset, data=request.data, partial=True)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def destroy(self, request, pk=None):
#       queryset = Category.objects.get(pk=pk)
#       items = OrderItem.objects.filter(food__category=queryset).count()
#       if items >= 1:
#          return Response({"detail":"Can not be deleted. The category is connected to the food in OrderItem"})
#       queryset.delete()
#       return Response({"message":"Category deleted successfully!"})


# Generic
# from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import mixins

# class CategoryGenericAPIView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
   # def get(self, request):
   #    return self.list(request)
   
   # def post(self, request):
   #    return self.create(request)

   # def get(self, request):
   #    queryset = self.get_queryset()
   #    serializer = self.get_serializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
   #    return Response(serializer.data)

   # def post(self, request):
   #    serializer = self.get_serializer(data = request.data)   # deserialization: covent json into model instance
   #    serializer.is_valid(raise_exception=True)
   #    serializer.save()
   #    return Response(serializer.data)

# class CategoryDetailGenericAPIView(GenericAPIView, RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
   # def get(self, request, *args, **kwargs):
   #    return self.retrieve(request, *args, **kwargs)
   
   # def put(self, request, *args, **kwargs):
   #    return self.update(request, *args, **kwargs)
   
   # def patch(self, request, *args, **kwargs):
   #    return self.partial_update(request, *args, **kwargs)
   
   # def delete(self, request, *args, **kwargs):
   #    instance = self.get_object()
   #    items = OrderItem.objects.filter(food__category=instance).count()
   #    if items >= 1:
   #       return Response({"detail":"Can not be deleted. The category is connected to the food in OrderItem"})
   #    return self.destroy(request, *args, **kwargs)




# APIView
# from rest_framework.views import APIView

# class CategoryAPIView(APIView):
#    def get(self, request):
#       queryset = Category.objects.all()
#       serializer = CategorySerializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
#       return Response(serializer.data)
   
#    def post(self, request):
#       serializer = CategorySerializer(data = request.data)   # deserialization: covent json into model instance
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# class CategoryDetailAPIView(APIView):
   # def get
   # def put
   # def patch
   # def delete

# function based
# @api_view(['GET'])
# def welcome(request):
#    return Response({"message":"Welcome to the RMS!"})

# @api_view(['GET','POST',])
# def category(request):
#    if request.method == 'POST':
#       serializer = CategorySerializer(data = request.data)   # deserialization: covent json into model instance
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
      
#    queryset = Category.objects.all()
#    serializer = CategorySerializer(queryset, many=True)     # serialize/ serializtion: convert qureyset/model instance/objects into json format 
#    return Response(serializer.data)


@api_view(['GET','PUT','PATCH','DELETE'])
def category_detail(request, id):
   queryset = Category.objects.get(id=id)
   
   if request.method == 'GET':
      serializer = CategorySerializer(queryset)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = CategorySerializer(queryset, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
   elif request.method == 'PATCH':
      serializer = CategorySerializer(queryset, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
   elif request.method == 'DELETE':
      items = OrderItem.objects.filter(food__category=queryset).count()
      if items >= 1:
         return Response({"detail":"Can not be deleted. The category is connected to the food in OrderItem"})
      queryset.delete()
      return Response({"message":"Category deleted successfully!"})

   # PUT request handle, PATCH request in category detail

# table ko endpoint: create, POST, PUT, PATCH, RETRIEVE