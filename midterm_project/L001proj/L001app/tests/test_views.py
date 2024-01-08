from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from L001app.models import NutritionalInformation, FoodItem, Restaurant, Review


class L001appTest(TestCase):
    def setUp(self):
        # Create instances for testing
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.food_item = FoodItem.objects.create(name='Test Food Item', restaurant=self.restaurant)
        self.food_item2 = FoodItem.objects.create(name='Test Food Item 2', restaurant=self.restaurant)
        self.nutritional_info = NutritionalInformation.objects.create(
            food_item=self.food_item,
            calories=100,
            cal_fat=10,
            total_fat=20,
            sat_fat=5.0,
            trans_fat=2.0,
            cholesterol=15,
            sodium=200,
            total_carb=30,
            fiber=5,
            sugar=10,
            protein=8
        )
        # API client for making requests
        self.client = APIClient()

    def test_add_restaurant(self):
        
        url = reverse('add_restaurant')
        data = {'name': 'New Restaurant'}
        # Sending a post method to add data
        response = self.client.post(url, data, format='json')

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testing the total data to know whether the post is successful 
        self.assertEqual(Restaurant.objects.count(), 2)

        # Testing all of the field added and seeing whether it is successfully added
        new_restaurant = Restaurant.objects.latest('id')
        self.assertEqual(new_restaurant.name, 'New Restaurant')
        print("Test test_add_restaurant passed")

    def test_add_fooditem(self):
        url = reverse('add_foodItem')
        data = {'restaurant_id':self.restaurant.id, 
                'name':'New Food'}
        # Sending a post method to add data
        response = self.client.post(url, data, format='json')

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testing the total data to know whether the post is successful 
        self.assertEqual(FoodItem.objects.count(), 3)

        # Testing all of the field added and seeing whether it is successfully added
        new_food_item = FoodItem.objects.latest('id')
        self.assertEqual(new_food_item.name, 'New Food')
        print("Test test_add_food_item passed")

    def test_add_nutrition(self):
        url = reverse('add_nutrition')
        data = {
            'food_item_id': self.food_item2.id,
            'calories': 150,
            'cal_fat': 15,
            'total_fat': 25,
            'sat_fat': 6.0,
            'trans_fat': 2.5,
            'cholesterol': 20,
            'sodium': 250,
            'total_carb': 35,
            'fiber': 6,
            'sugar': 12,
            'protein': 10
        }
         # Sending a post method to add data
        response = self.client.post(url, data, format='json')

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testing the total data to know whether the post is successful 
        self.assertEqual(NutritionalInformation.objects.count(), 2)

        # Testing all of the field added and seeing whether it is successfully added
        new_nutritional_info = NutritionalInformation.objects.latest('id')
        self.assertEqual(new_nutritional_info.calories, 150)
        self.assertEqual(new_nutritional_info.cal_fat, 15)
        self.assertEqual(new_nutritional_info.total_fat, 25)
        self.assertEqual(new_nutritional_info.sat_fat, 6.0)
        self.assertEqual(new_nutritional_info.trans_fat, 2.5)
        self.assertEqual(new_nutritional_info.cholesterol, 20)
        self.assertEqual(new_nutritional_info.sodium, 250)
        self.assertEqual(new_nutritional_info.total_carb, 35)
        self.assertEqual(new_nutritional_info.fiber, 6)
        self.assertEqual(new_nutritional_info.sugar, 12)
        self.assertEqual(new_nutritional_info.protein, 10)
        print("Test test_add_nutrition passed")


    def test_view_nutrition(self):
        url = reverse('view_nutrition', args=[self.nutritional_info.id])
        # Sending a get method to retrieve data
        response = self.client.get(url)
        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test view_nutrition passed")
        

    def test_view_food(self):
        url = reverse('view_food', args=[self.food_item.id])
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test view_foodItem passed")

    def test_view_restaurant(self):
        url = reverse('view_food', args=[self.restaurant.id])
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test view_restaurant passed")

    def test_delete_nutrition(self):
        url = reverse('delete_nutrition', args=[self.nutritional_info.id])
        # Sending a delete method to delete data
        response = self.client.delete(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Testing whether the data is successfully deleted or not
        self.assertFalse(NutritionalInformation.objects.filter(id=self.nutritional_info.id).exists())
        print("Test delete_nutrition passed")

    def test_delete_nutrition(self):
        url = reverse('delete_food_item', args=[self.nutritional_info.id])
        # Sending a delete method to delete data
        response = self.client.delete(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Testing whether the data is successfully deleted or not
        self.assertFalse(FoodItem.objects.filter(id=self.nutritional_info.id).exists())
        print("Test delete_food_item passed")


    def test_edit_nutrition(self):
        url = reverse('edit_nutrition', args=[self.nutritional_info.id])
        data = {
            'calories': 125,
            'cal_fat': 15,
            'total_fat': 25,
            'sat_fat': 6.0,
            'trans_fat': 2.5,
            'cholesterol': 20,
            'sodium': 250,
            'total_carb': 35,
            'fiber': 12,
            'sugar': 12,
            'protein': 10
        }
         # Sending a put method to update the data
        response = self.client.put(url, data, format='json')

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_nutritional_info = NutritionalInformation.objects.get(id=self.nutritional_info.id)
        # Testing all of the updated field and seeing whether it is successfully updated
        self.assertEqual(updated_nutritional_info.calories, 125)
        self.assertEqual(updated_nutritional_info.cal_fat, 15)
        self.assertEqual(updated_nutritional_info.total_fat, 25)
        self.assertEqual(updated_nutritional_info.sat_fat, 6.0)
        self.assertEqual(updated_nutritional_info.trans_fat, 2.5)
        self.assertEqual(updated_nutritional_info.cholesterol, 20)
        self.assertEqual(updated_nutritional_info.sodium, 250)
        self.assertEqual(updated_nutritional_info.total_carb, 35)
        self.assertEqual(updated_nutritional_info.fiber, 12)
        self.assertEqual(updated_nutritional_info.sugar, 12)
        self.assertEqual(updated_nutritional_info.protein, 10)
        print("Test edit_nutrition passed")


    def test_above_filter(self):
        url = reverse('above_filter', args=[90])
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the expected data
        self.assertTrue('calories' in response.data[0])

        # Testing the data is filtered correctly or not
        self.assertTrue(response.data[0]['calories'] > 90)
        print("Test above_filter passed")

    def test_below_filter(self):
        url = reverse('below_filter', args=[50])
        # Sending a get method to retrieve data
        response = self.client.get(url)
        
        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Checking data below 50 cal
        for i in response.data:
            self.assertNotIn('calories', i)
        print("Test below_filter passed")


    def test_find_word(self):
        url = reverse('find_word', args=['Test'])
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming the response contains a list of items
        for i in response.data:
            self.assertIn('name', i)
        print("Test find_word passed")


    def test_full_info(self):
        url = reverse('full_info')
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Testing the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response has all important data
        for item in response.data:
            self.assertIn('item_name', item)  
            self.assertIn('restaurant', item)  
            self.assertIn('calories', item)
        print("Test full_info passed")


    def test_reviews(self):
        url = reverse('review-list')
        # Sending a get method to retrieve data
        response = self.client.get(url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Testing the post method
        data = {'food_item': self.food_item.id, 'rating': 9, 'comment': 'Great food!'}
        response = self.client.post(url, data, format='json')
        # Check that the creation was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the new review is present in the list
        new_review_id = response.data.get('id')
        self.assertTrue(Review.objects.filter(id=new_review_id).exists())

        # Check that the newly created review has the expected content
        new_review = Review.objects.latest('id')
        self.assertEqual(new_review.food_item, self.food_item)
        self.assertEqual(new_review.rating, 9)
        self.assertEqual(new_review.comment, 'Great food!')
        print("Test reviews passed")