from django.contrib.auth.models import User
from .models import RecipePost
from rest_framework import status
from rest_framework.test import APITestCase


class RecipePostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='gagan', password='pass')

    def test_can_list_recipeposts(self):
        gagan = User.objects.get(username='gagan')
        RecipePost.objects.create(owner=gagan, name='wow')
        response = self.client.get('/Recipeposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipepost(self):
        self.client.login(username='gagan', password='pass')
        response = self.client.post('/Recipeposts/', {'name': 'wow'})
        count = RecipePost.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_recipepost(self):
        response = self.client.post('/Recipeposts/', {'name': 'wow'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipePostDetailViewTests(APITestCase):

    def setUp(self):
        gagan = User.objects.create_user(username='gagan', password='pass')
        RecipePost.objects.create(
            owner=gagan, name='wow', matter='adams content'
        )
    
    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/Recipeposts/1/')
        self.assertEqual(response.data['name'], 'wow')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipepost_using_valid_id(self):
        response = self.client.get('/Recipeposts/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

    

        


 
        
    