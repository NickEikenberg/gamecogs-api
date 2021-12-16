from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAccountSerializer
from .models import UserAccount

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.

class UserAccountList(generics.ListCreateAPIView):
  queryset = UserAccount.objects.all().order_by('id')
  serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = UserAccount.objects.all().order_by('id')
  serializer_class = UserAccountSerializer

## USER AUTH
def check_login(request):
  # If a GET request is made, return an empty object
  if request.method=='GET':
    return JsonResponse({})

  if request.method=='PUT':
    # Make the request JSON
    jsonRequest = json.loads(request.body)
    email = jsonRequest['email']
    password = jsonRequest['password']

    # See if email exists in DB
    if UserAccount.objects.get(email=email):
      user = UserAccount.objects.get(email=email)

      if check_password(password, user.password):
        return JsonResponse({'id': user.id, 'email': user.email})
      else:
        return JsonResponse({})
    else:
      return JsonResponse({})
