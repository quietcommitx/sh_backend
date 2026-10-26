from django.urls import path
from .views import *

urlpatterns = [
   # path('welcome/', welcome)
   # path('category/',category),
   path('category/<id>/',category_detail),
   # path('categories/', CategoryAPIView.as_view()),
   path('categories/', CategoryGenericAPIView.as_view()),
   path('categories/<pk>/', CategoryDetailGenericAPIView.as_view()),
   
]
