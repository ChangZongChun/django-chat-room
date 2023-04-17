from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.RoomsList),
    path('rooms/<str:pk>', views.getRoom),
    path('create-room/', views.createRoom),
]

