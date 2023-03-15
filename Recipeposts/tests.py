from django.contrib.auth.models import User
from .models import RecipePost
from rest_framework import status
from rest_framework.test import APITestCase


class RecipePostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_recipeposts(self):
        adam = User.objects.get(username='adam')
        RecipePost.objects.create(owner=adam, name='a title')
        response = self.client.get('/Recipeposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipepost(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/Recipeposts/', {'name': 'a title'})
        count = RecipePost.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_recipepost(self):
        response = self.client.post('/Recipeposts/', {'name': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipePostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        RecipePost.objects.create(
            owner=adam, name='a title', matter='adams content'
        )
        RecipePost.objects.create(
            owner=brian, name='another title', matter='brians content'
        )

    def test_can_retrieve_recipepost_using_valid_id(self):
        response = self.client.get('/Recipeposts/3/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipepost_using_invalid_id(self):
        response = self.client.get('/Recipeposts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipepost(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/Recipeposts/3/', {'name': 'a new title'})
        post = RecipePost.objects.filter(pk=3).first()
        self.assertEqual(Recipepost.name, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipepost(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/Recipeposts/3/', {'name': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
