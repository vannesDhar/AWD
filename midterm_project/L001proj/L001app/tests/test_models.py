# your_app/tests.py
from django.test import TestCase
from L001app.models import Restaurant, FoodItem, NutritionalInformation, Review

class YourModelTests(TestCase):
    def setUp(self):
        # Set up any necessary data for your tests

        # Create a test restaurant instance
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")

        # Create a test food item instance associated with the test restaurant
        self.food_item = FoodItem.objects.create(name="Test Food", restaurant=self.restaurant)

        # Create a test nutritional information instance associated with the test food item
        self.nutritional_info = NutritionalInformation.objects.create(
            food_item=self.food_item,
            calories=200,
            cal_fat=10,
            total_fat=15,
            sat_fat=5.5,
            trans_fat=1.2,
            cholesterol=20,
            sodium=300,
            total_carb=30,
            fiber=5,
            sugar=10,
            protein=25
        )

        # Create a test review instance associated with the test food item
        self.review = Review.objects.create(
            food_item=self.food_item,
            rating=8,
            comment="Good food!"
        )

    def test_restaurant_model(self):
        # Test the Restaurant model
        restaurant = Restaurant.objects.get(name="Test Restaurant")
        self.assertEqual(restaurant.name, "Test Restaurant")

    def test_food_item_model(self):
        # Test the FoodItem model
        food_item = FoodItem.objects.get(name="Test Food")
        self.assertEqual(food_item.name, "Test Food")
        self.assertEqual(food_item.restaurant, self.restaurant)

    def test_nutritional_information_model(self):
        # Test the NutritionalInformation model
        nutritional_info = NutritionalInformation.objects.get(food_item=self.food_item)
        self.assertEqual(nutritional_info.calories, 200)

    def test_review_model(self):
        # Test the Review model
        review = Review.objects.get(food_item=self.food_item)
        self.assertEqual(review.rating, 8)
        self.assertEqual(review.comment, "Good food!")

    
