from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAccountSerializer
from .serializers import UserListsSerializer
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

class UserGameLists(generics.RetrieveUpdateDestroyAPIView):
  queryset = UserAccount.objects.all().order_by('id')
  serializer_class = UserListsSerializer

  

### THIS IS THE FUNCTION THAT PERFORMS AUTH
def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        email = jsonRequest['email'] #get the email from the request
        password = jsonRequest['password'] #get the password from the request
        collection = jsonRequest['collection']
        forsale = jsonRequest['forsale']
        wantlist = jsonRequest['wantlist']
        try:
          if UserAccount.objects.get(email=email): #see if email exists in db
              user = UserAccount.objects.get(email=email)  #find user object with matching email
              if check_password(password, user.password): #check if passwords match
                  return JsonResponse({'id': user.id, 'email': user.email, 'collection': user.collection, 'forsale':user.forsale, 'wantlist':user.wantlist}) #if passwords match, return a user dict
              else: #passwords don't match so return empty dict
                  return JsonResponse({"error":"Passwords don't match!"})
          else: #if email doesn't exist in db, return empty dict
              return JsonResponse({"error":"No email found"})
        except:
          return JsonResponse({"error":"Email doesn't exist in our database"})
