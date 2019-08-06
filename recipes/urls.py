from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    path('recipes/', views.FoodRecipeList.as_view()),
    path('recipes/<int:pk>/', views.FoodRecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)