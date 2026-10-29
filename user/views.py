from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
# Create your views here.

class Login(APIView):
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username == "" or password == "":
         return Response({"error": "Username and password are required."}, status=400)
      user = authenticate(username = username, password = password)   #User.objects.filter(username=username, password=password).first()
      if user:
         return Response({"detail": "Valid user"}, status=200)
      else:
         return Response({"error": "Invalid username or password."}, status=401)