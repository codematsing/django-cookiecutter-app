# from django.test import TestCase
# from django.urls import resolve, reverse
# from {{cookiecutter.app_name}}.models import {{cookiecutter.snake_case_model_name}}
# from {{cookiecutter.app_name}}.tests.factories import {{cookiecutter.snake_case_model_name}}Factory

# class {{cookiecutter.snake_case_model_name}}UrlsTestCase(TestCase):

#     def setUp(self):
#         self.object = {{cookiecutter.snake_case_model_name}}Factory()

#     def test_list(self):
#         pass

#     def test_detail(self):
#         pass
#         # assert (
#         #     reverse("{{cookiecutter.app_name}}:detail", kwargs={"pk": self.object.pk})
#         #     == f"/users/{self.object.pk}/"
#         # )
#         # assert resolve(f"/users/{self.object.pk}/").view_name == "{{cookiecutter.app_name}}:detail"

#     def test_create(self):
#         pass

#     def test_update(self):
#         pass
#         # assert reverse("{{cookiecutter.app_name}}:update") == "/users/~update/"
#         # assert resolve("/users/~update/").view_name == "{{cookiecutter.app_name}}:update"

#     def test_delete(self):
#         pass

#     def test_redirect(self):
#         pass
#         # assert reverse("{{cookiecutter.app_name}}:redirect") == "/users/~redirect/"
#         # assert resolve("/users/~redirect/").view_name == "{{cookiecutter.app_name}}:redirect"

#     def tearDown(self):
#         pass