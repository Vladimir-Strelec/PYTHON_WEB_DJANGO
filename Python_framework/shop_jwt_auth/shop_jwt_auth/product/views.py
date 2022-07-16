from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from shop_jwt_auth.product.models import Product
from shop_jwt_auth.product.permission import CustomPermission
from shop_jwt_auth.product.serializers import ProductSerializer


class ProductGet(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPost(mixins.CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class ProductPut(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (CustomPermission,)
    authentication_classes = (TokenAuthentication,)


class ProductDelete(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (CustomPermission,)
    authentication_classes = (TokenAuthentication,)


