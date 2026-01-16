# pytest
import pytest

# rest_framework
from rest_framework import status

# local
from employees.models import Employee


pytestmark = pytest.mark.django_db


# --------------------
# AUTH REQUIRED
# --------------------
def test_authentication_required(api_client):
    response = api_client.get("/api/employees/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --------------------
# LIST EMPLOYEES
# --------------------
def test_list_employees(auth_client, employee):
    response = auth_client.get("/api/employees/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1


# --------------------
# RETRIEVE EMPLOYEE
# --------------------
def test_retrieve_employee(auth_client, employee):
    response = auth_client.get(f"/api/employees/{employee.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "amit@example.com"


# --------------------
# CREATE EMPLOYEE
# --------------------
def test_create_employee(auth_client):
    payload = {
        "name": "Neha Singh",
        "email": "neha@example.com",
        "department": "HR",
        "role": "Manager"
    }
    response = auth_client.post("/api/employees/", payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1


# --------------------
# DUPLICATE EMAIL (EDGE CASE)
# --------------------
def test_create_employee_with_existing_email(auth_client, employee):
    payload = {
        "name": "Duplicate",
        "email": "amit@example.com",
        "department": "Sales",
        "role": "Analyst"
    }
    response = auth_client.post("/api/employees/", payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data


# --------------------
# UPDATE EMPLOYEE
# --------------------
def test_update_employee(auth_client, employee):
    payload = {
        "name": "Amit Updated",
        "email": "amit@example.com",
        "department": "HR",
        "role": "Manager"
    }
    response = auth_client.put(
        f"/api/employees/{employee.id}/",
        payload
    )
    assert response.status_code == status.HTTP_200_OK

    employee.refresh_from_db()
    assert employee.department == "HR"


# --------------------
# DELETE EMPLOYEE
# --------------------
def test_delete_employee(auth_client, employee):
    response = auth_client.delete(
        f"/api/employees/{employee.id}/"
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Employee.objects.count() == 0
