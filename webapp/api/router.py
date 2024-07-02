from rest_framework.routers import (
    SimpleRouter
)
from rest_framework_nested.routers import (
    NestedSimpleRouter,
)
from api.view.user import (
    RegisterUserViewSet
)


v1_router = SimpleRouter(trailing_slash=False)

user_router = SimpleRouter(trailing_slash=False)
user_router.register("users", RegisterUserViewSet, basename="user")

v1_router.registry.extend(user_router.registry)
