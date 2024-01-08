from L001app.models import *
import csv

def run():
    with open('csvFiles/fastfood_calories.csv') as fastfood_calories:
        readCalories = csv.reader(fastfood_calories)
        next(readCalories)

        Restaurant.objects.all().delete()
        FoodItem.objects.all().delete()
        NutritionalInformation.objects.all().delete()

        for row in readCalories:
            if any(value == 'NA' for value in row[1:13]):
                continue
            
            restaurant, created = Restaurant.objects.get_or_create(name=row[1])
            food_item, created = FoodItem.objects.get_or_create(name=row[2], restaurant=restaurant)
            nutritionalInformation, created = NutritionalInformation.objects.get_or_create(food_item=food_item,
                                                            calories=row[3],
                                                            cal_fat=row[4],
                                                            total_fat=row[5],
                                                            sat_fat=row[6],
                                                            trans_fat=row[7],
                                                            cholesterol=row[8],
                                                            sodium=row[9],
                                                            total_carb=row[10],
                                                            fiber=row[11],
                                                            sugar=row[12],
                                                            protein=row[13]

                                                            )
            