from django.test import TestCase
from django.urls import resolve, reverse
from {{cookiecutter.app_name}}.models import {{cookiecutter.snake_case_model_name}}
from {{cookiecutter.app_name}}.tests.factories import {{cookiecutter.snake_case_model_name}}Factory
import logging
logger = logging.getLogger(__name__)

class {{cookiecutter.snake_case_model_name}}MdoelTestCase(TestCase):
    def setUp(self):
        self.object = {{cookiecutter.snake_case_model_name}}Factory()
        logger.info(f"{self.object} created")

    def test_case_one(self):
        pass

    def tearDown(self):
        pass
