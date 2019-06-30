from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Tasks

# Create your tests here.


class TasksTest(TestCase):

    def setUp(self):
        """Create a User and a Task to unittest"""
        user = User.objects.create(first_name='user', last_name='test',
                                   username='unittest', password='testando')
        Tasks.objects.create(creator=user, name='Test do terminal',
                             description='Continua nos teste',
                             finish_in='2020-04-04', priority=8)

    def test_create_task(self):
        """Checking some fields of new task"""
        user_created = User.objects.first()
        task_created = Tasks.objects.get(name='Test do terminal')

        self.assertEqual(task_created.creator, user_created)
        self.assertEqual(str(task_created), 'Test do terminal')
        self.assertEqual(task_created.priority, 8)
