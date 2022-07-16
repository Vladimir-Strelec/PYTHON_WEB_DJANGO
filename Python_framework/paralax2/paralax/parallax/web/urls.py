from django.urls import path

from parallax.web.views import CatalogView, CreateProductView, HomeTemplateView, EditProductView, InfoProductView, \
    DeleteProductView, add_comments_product, AllCommentsView

urlpatterns = (
    path('', HomeTemplateView.as_view(), name='index'),

    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('create/product/', CreateProductView.as_view(), name='create product'),
    path('edit/product/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('info/product/<int:pk>/', InfoProductView.as_view(), name='info product'),
    path('delete/product/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
    path('add/comment/product/<int:pk>/', add_comments_product, name='add comment'),
    path('comments/view/product/<int:pk>/', AllCommentsView.as_view(), name='all comment'),

)
