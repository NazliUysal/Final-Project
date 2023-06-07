from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profiles/<str:pk>/', views.profiles, name="profiles"),
    path('userlist/', views.userlist, name="userlist"),
    path('account/', views.useraccount, name="account"),
    path('account/edit-profile/', views.editaccount, name="edit-account"),
    path('favorites/<str:pk>', views.addtofavorites, name="addtofavorites"),
    path('account/favoritelist/', views.favoritelist, name="favoritelist"),
]
