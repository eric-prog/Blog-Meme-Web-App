from django.urls import path
from . import views

app_name = 'memes'

urlpatterns = [
    path('', views.meme_list, name = 'list'),
    path('create/', views.meme_create, name = 'create'),
    path('<slug:slug>/', views.meme_detail, name = 'detail'), 
]
