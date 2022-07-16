from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.contrib import admin
from django.urls import path, include, re_path

from shop_jwt_auth.product.views import ProductGet, ProductPost, ProductPut, ProductDelete

router = SimpleRouter()
router.register('product/list', ProductGet)
router.register('product/create', ProductPost)
router.register('product/update', ProductPut)
router.register('product/delete', ProductDelete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth_drf/', include('rest_framework.urls')),
    path('auth_register_djoser/', include('djoser.urls')),
    re_path('^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + router.urls
