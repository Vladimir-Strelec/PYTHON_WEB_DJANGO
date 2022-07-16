from django.urls import path

from audiu_library.web.views import AddAlbum, AlbumDetails, EditAlbum, DeleteAlbum, ProfileDetails, DeleteProfile, Home

urlpatterns = (
    path('', Home.as_view(), name='Home'),
    path('album/add/', AddAlbum.as_view(), name='AddAlbum'),
    path('album/details/<int:pk>/', AlbumDetails.as_view(), name='Album Details'),
    path('album/edit/<int:pk>/', EditAlbum),
    path('album/delete/<int:pk>/', DeleteAlbum),
    path('profile/details/', ProfileDetails),
    path('profile/delete/', DeleteProfile),

)