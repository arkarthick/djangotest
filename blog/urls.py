from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('posts-list/', views.post_list, name='post_list'),
    path('create-post', views.create_post, name='create_post'),
    path('view-post/<str:pk>/', views.view_post, name='view_post'),
    path('update-post/<str:pk>/', views.update_post, name='update_post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete_post'),
]
