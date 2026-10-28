from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'food', FoodModelViewSet, basename='food')

urlpatterns = [
   # path('welcome/', welcome)
   # path('category/',category),
   # path('category/<id>/',category_detail),
   # path('categories/', CategoryAPIView.as_view()),
   # path('categories/', CategoryViewSet.as_view({'get':'list','post':'create'})),
   # path('categories/<pk>/', CategoryDetailGenericAPIView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
   # path('categories/', CategoryModelViewSet.as_view({'get':'list','post':'create'})),
] + router.urls
