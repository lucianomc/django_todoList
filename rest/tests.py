from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from todo_list.models import Tasks

# Create your tests here.


class TaskAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create(first_name='user', last_name='test',
                                   username='testAPI')
        user.set_password('asdfjklç')
        user.save()

        task = Tasks.objects.create(creator=user, name='Test do terminal',
                                    description='Continua nos teste',
                                    finish_in='2020-04-04', priority=8)

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        task_count = Tasks.objects.count()
        self.assertEqual(task_count, 1)

    # def test_task_create(self):
    # def test_task_read(self):
    # def test_task_delete(self):
    # def test_task_list(self):