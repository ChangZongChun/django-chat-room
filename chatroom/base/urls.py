from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.inRoom, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('creat-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    path('update_user/', views.updateUser, name='update-user'),

    path('topics/', views.topicsPage, name='topics-page'),
    path('activities/', views.activityPage, name='activities-page'),

]
    