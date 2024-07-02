from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from rest_framework.request import (
        HttpRequest
    )

from rest_framework import status
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from rest_framework.response import (
    Response
)
from rest_framework.viewsets import (
    ViewSet,
)

from api.serializer.user import UserRegisterSerializer


class RegisterUserViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]

    def create(self, request: HttpRequest) -> Response:
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return exceptions.ValidationError("invalid field")

        user = serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )
