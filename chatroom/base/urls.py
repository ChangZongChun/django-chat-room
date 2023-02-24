from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.inRoom, name="room"),
    path('creat-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

]
    