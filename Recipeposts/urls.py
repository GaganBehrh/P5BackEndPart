from django.urls import path
from Recipeposts import views

urlpatterns = [
    path('Recipeposts/', views.RecipePostList.as_view()),
    path('Recipeposts/<int:pk>/', views.RecipePostDetail.as_view())
]