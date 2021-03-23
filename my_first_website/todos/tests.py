from django.test import TestCase
from .models import Todo

# Create your tests here.


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', content='a body here')

    def test_todo_title(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first todo')

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.content}'
        self.assertEqual(expected_object_name, 'a body here')
