from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        """
        Create a User
        """
        self.client = Client()
        self.user = User.objects.create_superuser(first_name='user',
                                                  last_name='test',
                                                  email='test@test.com.br',
                                                  username='unittest',
                                                  password='testando')

    def test_login(self):
        """Test login"""
        response = self.client.get(reverse('login'))
        user_login = self.client.post(
            '/login/', {'username': 'unittest', 'password': 'testando'})
        self.assertContains(response, 'Login')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(user_login)
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Entrar')

    def test_view_without_login(self):
        """Testing the redirect if user not logged"""
        response = self.client.get(reverse('todo_list:list_task'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/todolist/')
