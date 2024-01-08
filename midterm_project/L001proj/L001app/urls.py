from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
urlpatterns=[
    
    path('', views.ApiOverview, name='home'),
    path('', include(router.urls)),
    # Basic CRUD
    path('addNutrition/', views.add_nutrition, name='add_nutrition'),
    path('addRestaurant/', views.add_restaurant, name='add_restaurant'),
    path('addFoodItem/',views.add_foodItem, name='add_foodItem'),   
    path('viewNutrition/<int:resource_id>', views.view_nutrition, name='view_nutrition'),
    path('viewRestaurant/<int:resource_id>', views.view_restaurant, name='view_restaurant'),
    path('viewFoodItem/<int:resource_id>', views.view_food, name='view_food'),
    path('editNutrition/<int:resource_id>',views.edit_nutrition ,name='edit_nutrition'),
    path('deleteNutrition/<int:resource_id>', views.delete_nutrition, name='delete_nutrition'),
    path('deleteFoodItem/<int:resource_id>', views.delete_food_item, name='delete_food_item'),
    # Endpoints
    path('aboveFilter/<int:threshold_calories>',views.above_filter, name='above_filter'),
    path('belowFilter/<int:threshold_calories>',views.below_filter, name='below_filter'),
    path('nameFilter/<str:word>', views.find_word, name='find_word'),
    path('fullInfo/', views.full_info, name='full_info'),
    path('findRestaurant/<str:restaurant_name>', views.find_restaurant, name='find_restaurant'),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework')),
    
]