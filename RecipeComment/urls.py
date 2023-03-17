from django.urls import path
from RecipeComment import views

urlpatterns = [
    path('Recipecomment/', views.RecipeCommentList.as_view()),
    path('Recipecomment/<int:pk>/', views.RecipeCommentDetail.as_view())
]