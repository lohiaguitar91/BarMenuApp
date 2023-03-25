from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

# generates /recipes/ (CREATE | READ)
# generates /recipes/{id} (READ | UPDATE | DELETE)
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path("", include(router.urls))
]