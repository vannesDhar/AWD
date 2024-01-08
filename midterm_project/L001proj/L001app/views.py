from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import NutritionalInformation, FoodItem, Restaurant, Review
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        '++++++++++++++++++' :"BASIC CRUD:",
        'addNutrition': "http://localhost:8000/api/addNutrition",
        'addFoodItem' : "http://localhost:8000/api/addFoodItem",
        'addRestaurant' : "http://localhost:8000/api/addRestaurant",
        'viewNutrition' : "http://localhost:8000/api/viewNutrition/4500",
        'viewRestaurant' : "http://localhost:8000/api/viewRestaurant/71",
        'viewFoodItem' :"http://localhost:8000/api/viewFoodItem/4500",
        'editNutrition' : "http://localhost:8000/api/editNutrition/4500",
        'deleteNutrition' : "http://localhost:8000/api/deleteNutrition/4500",
        'deleteFoodItem': "http://localhost:8000/api/deleteFoodItem/4500",
        '------------------' :"ENDPOINTS:",
        
        'aboveFilter': "http://localhost:8000/api/aboveFilter/200",
        'belowFilter': "http://localhost:8000/api/belowFilter/1000",
        'nameFilter' : "http://localhost:8000/api/nameFilter/Cheese",
        'fullInfo' : "http://localhost:8000/api/fullInfo",
        'findRestaurant' : "http://localhost:8000/api/findRestaurant/Mcdonalds",
        'reviews':"http://localhost:8000/api/reviews"
    }
    return Response(api_urls)


@api_view(['POST','GET'])
def add_nutrition(request):

    if request.method == 'POST':
        # Validate for already existing data
        food_item_id = request.data.get('food_item_id')
        if NutritionalInformation.objects.filter(food_item_id=food_item_id).exists():
            return Response({'detail': 'Nutritional information for this food item already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new NutritionalInformation object
        nutritional_information = NutritionalInformation(
                                    food_item_id=food_item_id,           
                                    calories=request.data.get('calories'),   
                                    cal_fat=request.data.get('cal_fat'),     
                                    total_fat=request.data.get('total_fat'),  
                                    sat_fat=request.data.get('sat_fat'),      
                                    trans_fat=request.data.get('trans_fat'), 
                                    cholesterol=request.data.get('cholesterol'), 
                                    sodium=request.data.get('sodium'),          
                                    total_carb=request.data.get('total_carb'),  
                                    fiber=request.data.get('fiber'),            
                                    sugar=request.data.get('sugar'),           
                                    protein=request.data.get('protein'),    
        )   

        nutritional_information.save()
        serializer = NutritionalInformationSerializer(nutritional_information)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        # Creating structure for the input
        return Response({'food_item_id': '',
                        'calories': '',
                        'cal_fat': '',
                        'total_fat': '',
                        'sat_fat': '',
                        'trans_fat': '',    
                        'cholesterol': '',
                        'sodium': '',
                        'total_carb': '',
                        'fiber': '',
                        'sugar': '',
                        'protein': ''
        }, status=status.HTTP_200_OK)
    
@api_view(['POST','GET'])
def add_restaurant(request):
    if request.method=='POST':
        # Validate for already existing data
        if Restaurant.objects.filter(name=request.data.get('name')).exists():
            return Response({'detail': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Restaurant instance and set its attributes
        restaurant = Restaurant(name=request.data.get('name'))

        # Save the instance to the database
        restaurant.save()
        return Response({'detail': 'Restaurant added successfully'}, status=status.HTTP_201_CREATED)

    # Creating structure for the input
    if request.method=='GET':
        return Response({'name':''})
    
@api_view(['POST','GET'])
def add_foodItem(request):

    if request.method == 'POST':
        # Validate for already existing data
        food_item_name = request.data.get('name')
        restaurant_id = request.data.get('restaurant_id')
        if FoodItem.objects.filter(name=food_item_name, restaurant_id=restaurant_id).exists():
            return Response({'detail': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the instance for POST requests
        foodItem = FoodItem(name=request.data.get('name'), restaurant_id=request.data.get('restaurant_id'))
        foodItem.save()
        return Response({'detail': 'Food Item added successfully'}, status=status.HTTP_201_CREATED)
    
    # Creating structure for the input
    elif request.method == 'GET':
        return Response({'name' : '', 'restaurant_id': ''}, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_nutrition(request, resource_id):
    # Checking the availability of the data
    try:
        nutritional_Info = NutritionalInformation.objects.get(id=resource_id)
    except NutritionalInformation.DoesNotExist:
        return Response({'detail': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the retrieved nutritionalInformation instance
    serializer = NutritionalInformationSerializer(nutritional_Info)
    # Return the serialized data
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_restaurant(request, resource_id):
    try:
        restaurant = Restaurant.objects.get(id=resource_id)
    except Restaurant.DoesNotExist:
        return Response({'detail': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the retrieved restaurant instance
    serializer = RestaurantSerializer(restaurant)
    # Return the serialized data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_food(request, resource_id):
    try:
        foodItem = FoodItem.objects.get(id=resource_id)
    except FoodItem.DoesNotExist:
        return Response({'detail': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the retrieved food instance
    serializer = FoodItemSerializer(foodItem)
    # Return the serialized data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def edit_nutrition(request, resource_id):
    if request.method == 'GET':
        try:
            nutritional_info = NutritionalInformation.objects.get(id=resource_id)
            serializer = NutritionalInformationSerializer(nutritional_info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NutritionalInformation.DoesNotExist:
            return Response({'detail': 'Nutritional information not found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        try:
            nutritional_info = NutritionalInformation.objects.get(id=resource_id)

            # Update fields based on your request data
            nutritional_info.calories = request.data.get('calories', nutritional_info.calories)
            nutritional_info.cal_fat = request.data.get('cal_fat', nutritional_info.cal_fat)
            nutritional_info.total_fat = request.data.get('total_fat', nutritional_info.total_fat)
            nutritional_info.sat_fat = request.data.get('sat_fat', nutritional_info.sat_fat)
            nutritional_info.trans_fat = request.data.get('trans_fat', nutritional_info.trans_fat)
            nutritional_info.cholesterol = request.data.get('cholesterol', nutritional_info.cholesterol)
            nutritional_info.sodium = request.data.get('sodium', nutritional_info.sodium)
            nutritional_info.total_carb = request.data.get('total_carb', nutritional_info.total_carb)
            nutritional_info.fiber = request.data.get('fiber', nutritional_info.fiber)
            nutritional_info.sugar = request.data.get('sugar', nutritional_info.sugar)
            nutritional_info.protein = request.data.get('protein', nutritional_info.protein)

            # Save the changes
            nutritional_info.save()

            # Serialize the updated data and return it in the response
            serializer = NutritionalInformationSerializer(nutritional_info)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except NutritionalInformation.DoesNotExist:
            return Response({'detail': 'Nutritional information not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE','GET'])
def delete_nutrition(request, resource_id):
    if request.method == 'GET':
        # Validating the availability of the data based on the resource_id
        try:
            # If the data exist, serialize it then return the serialized data
            resource = NutritionalInformation.objects.get(id=resource_id)
            serializer = NutritionalInformationSerializer(resource)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If The data does not exist, return short message and the error status
        except NutritionalInformation.DoesNotExist:
            return Response({'detail': 'Nutritional information not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Handling when delete method is called
    elif request.method == 'DELETE':
        # Getting the searched object
        resource = NutritionalInformation.objects.get(id=resource_id)
        resource.delete()
        return Response({'detail': 'Entry is deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE','GET'])
def delete_food_item(request, resource_id):
    if request.method == 'GET':
        # Validating the availability of the data based on the resource_id
        try:
            # If the data exist, serialize it then return the serialized data
            foodItem = FoodItem.objects.get(id=resource_id)
            serializer = FoodItemSerializer(foodItem)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If The data does not exist, return short message and the error status
        except FoodItem.DoesNotExist:
            return Response({'detail': 'Food item information not found'}, status=status.HTTP_404_NOT_FOUND)

    # Handling when delete method is called 
    elif request.method == 'DELETE':
      # Getting the searched object
        foodItem = FoodItem.objects.get(id=resource_id)
        foodItem.delete()
        return Response({'detail': 'Entry is deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def above_filter(request,threshold_calories):
    try:
        filtered_data = NutritionalInformation.objects.filter(calories__gt=threshold_calories)
        serializer = NutritionalInformationSerializer(filtered_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'detail': 'Invalid threshold_calories value'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def below_filter(request,threshold_calories):
    try:
        filtered_data = NutritionalInformation.objects.filter(calories__lt=threshold_calories)
        serializer = NutritionalInformationSerializer(filtered_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'detail': 'Invalid threshold_calories value'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def find_word(request, word):
    # Checking all of the data that contains the word
    try:
        # Creating an object of filtered data by word
        items_with_word = FoodItem.objects.filter(name__icontains=word)

        # Serialize the data and return it
        serializer = FoodItemWithCaloriesSerializer(items_with_word, many=True)
        return Response(serializer.data)
    
    # If there is no food containing the word, we raise an error
    except ValueError:
        return Response({'No food containing this word'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def full_info(request):
    try:
        # Finding all of the related data in the models, This will change the id's of foreign key to their information
        data = NutritionalInformation.objects.select_related('food_item__restaurant').all()
        serializer = FullInfoSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Showing encountered error
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def find_restaurant(request, restaurant_name):
    try:
        # Get the restaurant by name
        restaurant = Restaurant.objects.get(name=restaurant_name)
        # Get all food items from the specified restaurant
        food_items = FoodItem.objects.filter(restaurant_id=restaurant.id)

        # Serialize the data
        serializer = FoodItemWithCaloriesSerializer(food_items, many=True)
        
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    

# Using the available modelViewSet 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

