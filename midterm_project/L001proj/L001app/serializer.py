from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

# Serializer for FoodItem with additional field for the restaurant name
class FoodItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(source='restaurant.name')  # Display the name of the restaurant
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'restaurant')

# Serializer for NutritionalInformation model
class NutritionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalInformation
        fields = ('id', 'food_item_id', 'calories', 'cal_fat', 'total_fat', 'trans_fat', 'cholesterol', 'sodium', 'fiber', 'protein', 'sugar', 'sat_fat', 'total_carb')

# Serializer for displaying full information including restaurant and food item names
class FullInfoSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(source='food_item.restaurant.name')  # Display the restaurant name
    item_name = serializers.CharField(source='food_item.name')  # Display the food item name

    class Meta:
        model = NutritionalInformation
        fields = ('id', 'item_name', 'restaurant', 'calories', 'cal_fat', 'total_fat', 'trans_fat', 'cholesterol', 'sodium', 'fiber', 'protein', 'sugar', 'sat_fat', 'total_carb')

# Serializer for FoodItem with an additional field for calories
class FoodItemWithCaloriesSerializer(serializers.ModelSerializer):
    calories = serializers.IntegerField(source='nutritionalinformation.calories', read_only=True)  # Display the calories

    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'calories']

# Serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'food_item', 'rating', 'comment', 'timestamp')
