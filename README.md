# Employee Management System

This project is an Employee Management System built using Django Rest Framework. It provides a RESTful API for managing employee records, including functionalities for creating, retrieving, updating, and deleting employee data. The project also implements JWT authentication for secure access.

## Features

- User login with JWT authentication.
- CRUD operations for employee records.
- PostgreSQL database for data storage.
- Simple and clean API endpoints for easy integration.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework
- PostgreSQL
- `djangorestframework-simplejwt` for JWT authentication

## Installation

## 1. Clone the Repository
git clone <repository-url>
cd employee-management-system

2. Install Dependencies
   pip install -r requirements.txt

3. Configure PostgreSQL Database
   Create a Database: Log into PostgreSQL and create a database.
   CREATE DATABASE Employee;
   Update Database Settings: In settings.py, update the DATABASES setting with your PostgreSQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Employee',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


5. Run Migrations
   python manage.py migrate
6. Create a Superuser
   python manage.py createsuperuser
7. Run the Development Server
   python manage.py runserver

The server will be running at http://127.0.0.1:8000/.

API Endpoints
Authentication
Login:
  POST /api/token/
Body:
{
    "username": "your_username",
    "password": "your_password"
}

Token Refresh:
  POST /api/token/refresh/
Body:
{
    "refresh": "your_refresh_token"
}

Employee Management
List Employees:
  GET /api/employees/

Create Employee:
 POST /api/employees/

 Body:
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "salary": 50000,
    "phone": {"number":"7700359739"} // This should be a valid foreign key ID
}


Retrieve Employee:
 GET /api/employees/<int:pk>/

Update Employee:
  PUT /api/employees/<int:pk>/
  Body:
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "salary": 60000,
    "phone": {"number":"7700359739"}
}

Delete Employee:
  DELETE /api/employees/<int:pk>/

Testing with Postman
1.Set Up Postman: Open Postman and create a new collection for your API.

2.Login:
 Create a POST request to /api/token/ with your credentials to obtain the JWT token.

3.Use JWT Token:
 For all subsequent requests, include the JWT token in the headers:
  Authorization: Bearer your_access_token

4.CRUD Operations:
  Use the above API endpoints to test the CRUD operations. Make sure to set the correct HTTP method and URL.

Notes
Ensure that your PostgreSQL service is running before starting the Django server.
All employee records should have valid foreign key references for the phone_number field.
If you encounter a "Not Found" error, double-check your URLs and ensure the server is running.


Acknowledgments
  Django
  Django Rest Framework
  PostgreSQL
