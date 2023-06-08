from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profiles/<str:pk>/', views.profiles, name="profiles"),
    path('userlist/', views.userlist, name="userlist"),
    path('account/', views.useraccount, name="account"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name="users/change-password.html"), name="change-password"),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name="users/passwordchangedone.html"), name="password_change_done"),
    path('account/edit-profile/', views.editaccount, name="edit-account"),
    path('favorites/<str:pk>', views.addtofavorites, name="addtofavorites"),
    path('account/favoritelist/', views.favoritelist, name="favoritelist"),
]
