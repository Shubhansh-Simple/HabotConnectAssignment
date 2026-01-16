# pytest
import pytest

# django
from django.contrib.auth import get_user_model

# rest_framework
from rest_framework.test import APIClient

# local
from employees.models import Employee


User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="testpass123"
    )


@pytest.fixture
def auth_client(api_client, user):
    response = api_client.post(
        "/login/",
        {"username": "testuser", "password": "testpass123"},
        format="json"
    )
    token = response.data["access"]
    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )
    return api_client


@pytest.fixture
def employee(db):
    return Employee.objects.create(
        name="Amit Verma",
        email="amit@example.com",
        department="Engineering",
        role="Developer"
    )
