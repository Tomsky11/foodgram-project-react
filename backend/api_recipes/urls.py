from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import FavoriteViewSet

router = DefaultRouter()

router.register('ingredients', views.IngredientsViewSet,
                basename='ingredients')
router.register('tags', views.TagsViewSet, basename='tags')
router.register('recipes', views.RecipeViewSet, basename='recipes')


urlpatterns = [
     path('recipes/<int:recipe_id>/favorite/',
          FavoriteViewSet.as_view(), name='favorite'),
    # path('recipes/<int:recipe_id>/shopping_cart/',
     #    ShoppingCartViewSet.as_view(), name='shopping_cart'),
     path('', include(router.urls)),
]
