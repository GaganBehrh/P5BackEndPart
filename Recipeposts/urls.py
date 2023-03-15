from django.urls import path
from Recipeposts import views

urlpatterns = [
    path('Recipeposts/', views.RecipePostList.as_view()),
]