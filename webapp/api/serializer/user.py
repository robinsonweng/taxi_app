from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser


from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password must match")
        return data

    def create(self, validated_data: dict) -> AbstractUser:
        data = {}
        for key, value in validated_data.items():
            if key in ("password", "confirm_password"):
                continue

            data.update({key: value})

        data["password"] = validated_data["password"]

        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }
