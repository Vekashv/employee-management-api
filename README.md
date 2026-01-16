# Employee Management REST API

A Django REST Framework-based API for managing employees in a company. This API provides full CRUD operations with JWT authentication, filtering, pagination, and comprehensive error handling.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Postman Testing Guide](#postman-testing-guide)

## ✨ Features

- **CRUD Operations**: Create, Read, Update, and Delete employees
- **JWT Authentication**: Secure token-based authentication for all endpoints
- **Validation**: Email uniqueness and name validation
- **Filtering**: Filter employees by department and role
- **Pagination**: 10 employees per page with pagination support
- **Error Handling**: Proper HTTP status codes (201, 400, 404, 204)
- **Comprehensive Testing**: Unit tests for all endpoints and edge cases
- **RESTful Design**: Follows REST principles with proper HTTP methods

## 🛠 Technology Stack

- **Python 3.8+**
- **Django 4.2.7**
- **Django REST Framework 3.14.0**
- **JWT Authentication** (djangorestframework-simplejwt)
- **SQLite** (default, can be switched to PostgreSQL)
- **Pytest** for testing

## 📁 Project Structure

```
employee_management/
├── employee_management/      # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── employees/                # Employees app
│   ├── __init__.py
│   ├── models.py             # Employee model
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   ├── urls.py               # App URL routes
│   ├── admin.py              # Django admin configuration
│   ├── apps.py
│   └── tests.py              # Unit tests
├── manage.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd "Employee Management"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for Django admin, optional):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/api
```

### Authentication

All endpoints require JWT authentication. First, obtain a token:

#### Get JWT Token
```http
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Note:** You need to create a user first. Use Django admin or create one programmatically:
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
User.objects.create_user(username='testuser', password='testpass123')
```

#### Refresh Token
```http
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token"
}
```

### Employee Endpoints

#### 1. Create Employee
```http
POST /api/employees/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer",
    "date_joined": "2025-01-09"
}
```

**Error Response (400 Bad Request):**
```json
{
    "email": ["An employee with this email already exists."]
}
```

#### 2. List All Employees
```http
GET /api/employees/
Authorization: Bearer {access_token}
```

**Query Parameters:**
- `department`: Filter by department (e.g., `?department=Engineering`)
- `role`: Filter by role (e.g., `?role=Developer`)
- `page`: Page number for pagination (e.g., `?page=2`)

**Response (200 OK):**
```json
{
    "count": 25,
    "next": "http://127.0.0.1:8000/api/employees/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "Engineering",
            "role": "Developer",
            "date_joined": "2025-01-09"
        },
        ...
    ]
}
```

#### 3. Retrieve Single Employee
```http
GET /api/employees/{id}/
Authorization: Bearer {access_token}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer",
    "date_joined": "2025-01-09"
}
```

**Error Response (404 Not Found):**
```json
{
    "detail": "Employee not found."
}
```

#### 4. Update Employee
```http
PUT /api/employees/{id}/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "name": "John Updated",
    "email": "john.updated@example.com",
    "department": "Sales",
    "role": "Manager"
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "name": "John Updated",
    "email": "john.updated@example.com",
    "department": "Sales",
    "role": "Manager",
    "date_joined": "2025-01-09"
}
```

#### 5. Delete Employee
```http
DELETE /api/employees/{id}/
Authorization: Bearer {access_token}
```

**Response (204 No Content):** Empty response body

**Error Response (404 Not Found):**
```json
{
    "detail": "Employee not found."
}
```

### HTTP Status Codes

- `200 OK`: Successful GET or PUT request
- `201 Created`: Successful POST request (employee created)
- `204 No Content`: Successful DELETE request
- `400 Bad Request`: Validation error (e.g., duplicate email, empty name)
- `401 Unauthorized`: Missing or invalid authentication token
- `404 Not Found`: Employee with given ID not found

## 🧪 Testing

### Run Tests

Using pytest:
```bash
pytest
```

Or using Django's test runner:
```bash
python manage.py test
```

### Test Coverage

The test suite covers:
- ✅ Creating employees with valid data
- ✅ Creating employees with duplicate emails (400 error)
- ✅ Creating employees with empty names (400 error)
- ✅ Creating employees with invalid emails (400 error)
- ✅ Listing all employees
- ✅ Pagination (10 per page)
- ✅ Filtering by department
- ✅ Filtering by role
- ✅ Retrieving a single employee
- ✅ Retrieving non-existent employee (404 error)
- ✅ Updating an employee
- ✅ Updating non-existent employee (404 error)
- ✅ Deleting an employee (204 response)
- ✅ Deleting non-existent employee (404 error)
- ✅ Authentication requirement
- ✅ Auto-generated date_joined field

## 📮 Postman Testing Guide

### Step 1: Set Up Postman

1. Open Postman
2. Create a new collection: "Employee Management API"

### Step 2: Authentication Setup

#### Get Access Token
1. Create a new request: `POST http://127.0.0.1:8000/api/token/`
2. Go to **Body** tab → Select **raw** → Choose **JSON**
3. Enter:
   ```json
   {
       "username": "testuser",
       "password": "testpass123"
   }
   ```
4. Send request
5. Copy the `access` token from the response

#### Configure Authorization
1. In your collection, go to **Authorization** tab
2. Select **Type**: Bearer Token
3. Paste your access token in the **Token** field
4. This will apply to all requests in the collection

### Step 3: Test Endpoints

#### Create Employee (POST /api/employees/)
1. Method: **POST**
2. URL: `http://127.0.0.1:8000/api/employees/`
3. Body (raw JSON):
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "department": "Engineering",
       "role": "Developer"
   }
   ```
4. Expected: **201 Created** with employee data

**Test Duplicate Email:**
- Use the same email again
- Expected: **400 Bad Request** with error message

#### List Employees (GET /api/employees/)
1. Method: **GET**
2. URL: `http://127.0.0.1:8000/api/employees/`
3. Expected: **200 OK** with paginated results

**Test Filtering:**
- URL: `http://127.0.0.1:8000/api/employees/?department=Engineering`
- Expected: Only Engineering employees

- URL: `http://127.0.0.1:8000/api/employees/?role=Developer`
- Expected: Only Developer employees

**Test Pagination:**
- URL: `http://127.0.0.1:8000/api/employees/?page=2`
- Expected: Second page of results

#### Retrieve Employee (GET /api/employees/{id}/)
1. Method: **GET**
2. URL: `http://127.0.0.1:8000/api/employees/1/` (use actual ID)
3. Expected: **200 OK** with employee data

**Test 404 Error:**
- URL: `http://127.0.0.1:8000/api/employees/999/`
- Expected: **404 Not Found**

#### Update Employee (PUT /api/employees/{id}/)
1. Method: **PUT**
2. URL: `http://127.0.0.1:8000/api/employees/1/`
3. Body (raw JSON):
   ```json
   {
       "name": "John Updated",
       "email": "john.updated@example.com",
       "department": "Sales",
       "role": "Manager"
   }
   ```
4. Expected: **200 OK** with updated data

#### Delete Employee (DELETE /api/employees/{id}/)
1. Method: **DELETE**
2. URL: `http://127.0.0.1:8000/api/employees/1/`
3. Expected: **204 No Content** (empty response)

### Step 4: Test Authentication

1. Remove the Bearer token from Authorization
2. Try any endpoint
3. Expected: **401 Unauthorized**

## 📝 Employee Model Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | Integer | Auto | Unique identifier (auto-generated) |
| `name` | String | Yes | Employee name (cannot be empty) |
| `email` | Email | Yes | Employee email (must be unique and valid) |
| `department` | String | No | Department (e.g., "HR", "Engineering", "Sales") |
| `role` | String | No | Role (e.g., "Manager", "Developer", "Analyst") |
| `date_joined` | Date | Auto | Date when employee joined (auto-generated) |

## 🔒 Security Notes

- All endpoints require JWT authentication
- Tokens expire after 1 hour (configurable in settings)
- Use refresh tokens to obtain new access tokens
- In production, change `SECRET_KEY` and set `DEBUG = False`
- Use environment variables for sensitive configuration

## 📞 Support

For questions or issues, please contact:
- Email: hr4@habot.io

## 📄 License

This project is created for HabotConnect DMCC hiring assessment.

---

**Built with ❤️ for HabotConnect DMCC**

