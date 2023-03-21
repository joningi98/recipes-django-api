from django.urls import path
from rest_framework import routers
from .views import PostList, PostDetail

a

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    
    path('', views.getData),
    path('add/', views.addRecipe)
]
