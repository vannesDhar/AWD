from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

# Food model
class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# Nutrition Information model
class NutritionalInformation(models.Model):
    food_item = models.OneToOneField(FoodItem, on_delete=models.CASCADE)
    calories = models.IntegerField()
    cal_fat = models.IntegerField()
    total_fat = models.IntegerField()
    sat_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    total_carb= models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __str__(self):
        return self.food_item
    
# Review model
class Review(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item.name} - {self.rating}"
    
    