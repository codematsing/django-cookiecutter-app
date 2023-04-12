import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory
from {{cookiecutter.app_name}}.tests.factories import {{cookiecutter.snake_case_model_name}}Factory
from {{cookiecutter.app_name}}.views import (
    {{cookiecutter.snake_case_model_name}}ListView,
    {{cookiecutter.snake_case_model_name}}DetailView,
    {{cookiecutter.snake_case_model_name}}UpdateView,
    {{cookiecutter.snake_case_model_name}}DeleteView,
)
import logging
logger = logging.getLogger(__name__)

class {{cookiecutter.snake_case_model_name}}ViewTestCase(TestCase):

    def setUp(self):
        self.object = {{cookiecutter.snake_case_model_name}}Factory()
        logger.info(f"{self.object} created")

    def test_get_success_url(self):
        pass
        # view = {{cookiecutter.snake_case_model_name}}UpdateView()
        # request = rf.get("/fake-url/")
        # request.user = user

        # view.request = request

        # assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self):
        pass
        # view = {{cookiecutter.snake_case_model_name}}UpdateView()
        # request = rf.get("/fake-url/")
        # request.user = user

        # view.request = request

        # assert view.get_object() == user

    def test_form_valid(self):
        pass
        # view = {{cookiecutter.snake_case_model_name}}UpdateView()
        # request = rf.get("/fake-url/")

        # # Add the session/message middleware to the request
        # SessionMiddleware(self.dummy_get_response).process_request(request)
        # MessageMiddleware(self.dummy_get_response).process_request(request)
        # request.user = user

        # view.request = request

        # # Initialize the form
        # form = UserAdminChangeForm()
        # form.cleaned_data = {}
        # form.instance = user
        # view.form_valid(form)

        # messages_sent = [m.message for m in messages.get_messages(request)]
        # assert messages_sent == ["Information successfully updated"]

    def test_redirect_view(self):
        pass
        # view = UserRedirectView()
        # request = rf.get("/fake-url")
        # request.user = user

        # view.request = request

        # assert view.get_redirect_url() == f"/users/{user.username}/"

    def test_detail_view_user_authenticated(self):
        pass
        # request = rf.get("/fake-url/")
        # request.user = UserFactory()

        # response = user_detail_view(request, username=user.username)

        # assert response.status_code == 200

    def test_detail_view_user_not_authenticated(self):
        pass
        # request = rf.get("/fake-url/")
        # request.user = AnonymousUser()

        # response = user_detail_view(request, username=user.username)
        # login_url = reverse(settings.LOGIN_URL)

        # assert isinstance(response, HttpResponseRedirect)
        # assert response.status_code == 302
        # assert response.url == f"{login_url}?next=/fake-url/"


    def tearDown(self):
        pass