from django.db import models
from rest_framework import serializers
from .models import UserAccount



from django.contrib.auth.hashers import make_password, check_password

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password', 'collection', 'forsale', 'wantlist')

    def create(self, validated_data):
        user = UserAccount.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance, validated_data):
        user = UserAccount.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.collection = validated_data["collection"]
        user.forsale = validated_data["forsale"]
        user.wantlist = validated_data["wantlist"]
        user.save()
        return user
    

class UserListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'collection', 'forsale', 'wantlist')

    def patch(self, instance, validated_data, partial=True):
        user = UserAccount.objects.get(email=validated_data["email"])
        user.collection = validated_data["collection"]
        user.forsale = validated_data["forsale"]
        user.wantlist = validated_data["wantlist"]
        user.save()
        return user

