from django.urls import path
from . import views

urlpatterns = [
    path('timeline/', views.timeline, name="timeline"),
    path('posts/<str:pk>', views.post_details, name="postdetails"),
    path('upload/', views.upload, name="upload"),
    path('delete/<str:pk>', views.deletePost, name="delete"),
    path('like/<str:pk>', views.likePost, name="like_post"),
    
]
