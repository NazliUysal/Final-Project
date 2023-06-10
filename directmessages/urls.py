from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.listThreads, name="inbox"),
    path('inbox/create-thread/', views.createThread, name="create-thread"),
    path('inbox/<int:pk>/', views.thread, name="thread"),
    path('inbox/<int:pk>/create-message/', views.createMessage, name="create-message"),
]