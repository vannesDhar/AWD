from django.contrib import admin
from .models import NutritionalInformation, Restaurant, FoodItem

# Registering models
admin.site.register(NutritionalInformation)
admin.site.register(Restaurant)
admin.site.register(FoodItem)
