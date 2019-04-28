from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('tracks/', views.track_list, name='track_list'),
    path('tracks/<int:pk>/', views.track_detail, name='track_detail'),
    path('tracks/new/', views.track_new, name='track_new'),

    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/new/', views.lesson_new, name='lesson_new'),
]