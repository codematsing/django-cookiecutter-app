from django.test import TestCase
from {{cookiecutter.app_name}}.models import {{cookiecutter.snake_case_model_name}}
from {{cookiecutter.app_name}}.tests.factories import {{cookiecutter.snake_case_model_name}}Factory

class {{cookiecutter.snake_case_model_name}}SignalTestCase(TestCase):

    def setUp(self):
        pass

    def test_case_one(self):
        pass

    def tearDown(self):
        pass