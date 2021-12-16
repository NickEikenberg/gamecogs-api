from rest_framework import serializers
from .models import UserAccount

from django.contrib.auth.hashers import make_password, check_password

class UserAccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserAccount
    fields = ('id', 'email', 'password', )

    def create(self, validated_data):
      user = UserAccount.objects.create(
        email = validated_data['email'],
        password = make_password(validated_data['password'])
      )
      user.save()
      return {"id": user.id, "email":user.email, "password": ""}

    def update(self, instance, validated_data):
      # user = UserAccount.objects.get(email=validated_data['email'])
      user = UserAccount.objects.get(id=instance.id)
      user.email = validated_data['email']
      user.password = make_password(validated_data['password'])
      user.save()
      return user