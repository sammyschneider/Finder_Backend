from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
# from .views import redirect_view


urlpatterns = [
    path('api/foods', views.FoodList.as_view(), name='food_list'),
    path('api/foods/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),
]
