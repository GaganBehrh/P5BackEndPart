from django.urls import path
from Recipeposts import views

urlpatterns = [
    path('Recipecomment/', views.RecipePostList.as_view()),
    path('Recipecomment/<int:pk>/', views.RecipePostDetail.as_view())
]