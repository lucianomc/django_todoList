from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from todo_list.models import Tasks

# Create your tests here.


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='user', last_name='test',
                                        username='testAPI')
        self.user.set_password('asdfjklç')
        self.user.save()

        task = Tasks.objects.create(creator=self.user, name='Test do terminal',
                                    description='Continua nos teste',
                                    finish_in='2020-04-04', priority=8)

    def test_single_user(self):
        self.assertEqual(User.objects.count(), 1)
        # Because F() expressions
        self.assertNotEqual(User.objects.first().id, 1)

    def test_single_post(self):
        self.assertEqual(Tasks.objects.count(), 1)
        # Because F() expressions
        self.assertNotEqual(Tasks.objects.first().id, 1)

    def test_list_task(self):
        data = {}
        url = reverse('rest:task_list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_task(self):
        self.assertTrue(self.client.login(
            username='testAPI', password='asdfjklç'))

        data = {"creator": self.user.pk, "name": "Test",
                "description": "Continua",
                "finish_in": "2020-04-04", "priority": 8}

        url = reverse('rest:task_create')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        task = Tasks.objects.last()

        self.assertEqual(Tasks.objects.count(), 2)
        self.assertEqual(task.id, 3)
        self.assertEqual(task.name, 'Test')
        self.assertEqual(task.priority, 8)

    # def test_task_read(self):
    # def test_task_delete(self):
