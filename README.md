# Employee Management API – Postman Demonstration

## Intro

This API provides **CRUD (Create, Read, Update, Delete)** functionality for managing employees in an organization. It is built using **Django REST Framework** and secured with **JWT (SimpleJWT)** authentication. The API follows RESTful best practices, supports pagination and filtering, and returns clear HTTP status codes for success and error cases.

---

## 🔐 Authentication

### Obtain JWT Token

**Endpoint**

```
POST /login/
```

**Request Body (JSON)**

```json
{
  "username": "admin",
  "password": "adminpassword"
}
```

**Successful Response (200 OK)**

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

---

### Add Token in Postman

1. Open Postman
2. Go to **Authorization** tab
3. Select **Type**: Bearer Token
4. Paste the **access token**

All subsequent API requests will now be authenticated.

---

## 📌 Endpoint Demonstrations

### 1️⃣ Create Employee

**Endpoint**

```
POST /api/employees/
```

**Request Body**

```json
{
  "name": "Amit Verma",
  "email": "amit@example.com",
  "department": "Engineering",
  "role": "Developer"
}
```

**Success Response (201 Created)**

```json
{
  "id": 1,
  "name": "Amit Verma",
  "email": "amit@example.com",
  "department": "Engineering",
  "role": "Developer",
  "date_joined": "2026-01-16"
}
```

---

#### ❌ Duplicate Email Case

**Request** (same email again)

```json
{
  "name": "Duplicate User",
  "email": "amit@example.com",
  "department": "HR",
  "role": "Manager"
}
```

**Error Response (400 Bad Request)**

```json
{
  "email": ["employee with this email already exists."]
}
```

---

### 2️⃣ List Employees

**Endpoint**

```
GET /api/employees/
```

**Paginated Response (200 OK)**

```json
{
  "count": 12,
  "next": "/api/employees/?page=2",
  "previous": null,
  "results": [...]
}
```

---

#### Filtering Examples

* By department:

```
GET /api/employees/?department=HR
```

---

### 3️⃣ Retrieve Single Employee

**Endpoint**

```
GET /api/employees/{id}/
```

**Success Response (200 OK)**

```json
{
  "id": 1,
  "name": "Amit Verma",
  "email": "amit@example.com",
  "department": "Engineering",
  "role": "Developer",
  "date_joined": "2026-01-16"
}
```

---

#### ❌ Non-existent Employee

```
GET /api/employees/999/
```

**Error Response (404 Not Found)**

```json
{
  "detail": "Not found."
}
```

---

### 4️⃣ Update Employee

**Endpoint**

```
PUT /api/employees/{id}/
```

**Request Body**

```json
{
  "name": "Amit Verma",
  "email": "amit@example.com",
  "department": "HR",
  "role": "Manager"
}
```

**Success Response (200 OK)**

```json
{
  "id": 1,
  "name": "Amit Verma",
  "email": "amit@example.com",
  "department": "HR",
  "role": "Manager",
  "date_joined": "2026-01-16"
}
```

---

### 5️⃣ Delete Employee

**Endpoint**

```
DELETE /api/employees/{id}/
```

**Success Response**

```
204 No Content
```

The employee is permanently removed from the system.

---

## ✅ Summary

* Demonstrated full **CRUD operations** using RESTful endpoints
* Implemented **JWT-based authentication** for secure access
* Proper **HTTP status codes** used (200, 201, 400, 401, 404, 204)
* Pagination and filtering improve performance and usability
* Postman provides an easy and effective way to test and validate APIs

This project demonstrates clean backend design, strong error handling, and production-ready API practices suitable for a Python Backend Developer role.
