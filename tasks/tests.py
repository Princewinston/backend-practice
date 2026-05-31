from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task as Todo


class TodoTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="prince",
            password="test123"
        )

        self.client.force_authenticate(
            user=self.user
        )

    def test_create_todo(self):
        todo = Todo.objects.create(
            user=self.user,
            title="Learn Django"
        )

        self.assertEqual(
            todo.title,
            "Learn Django"
        )

    def test_todo_list_page(self):
        response = self.client.get('/tasks/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_todo(self):
        todo = Todo.objects.create(
            user=self.user,
            title="Old Task"
        )

        todo.title = "Updated Task"
        todo.save()

        updated = Todo.objects.get(id=todo.id)

        self.assertEqual(
            updated.title,
            "Updated Task"
        )

    def test_delete_todo(self):
        todo = Todo.objects.create(
            user=self.user,
            title="Delete Me"
        )

        todo.delete()

        self.assertEqual(
            Todo.objects.count(),
            0
        )