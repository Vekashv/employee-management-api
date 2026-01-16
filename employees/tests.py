from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee
from datetime import date


class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_employee_success(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().name, 'John Doe')
        self.assertEqual(Employee.objects.get().email, 'john.doe@example.com')

    def test_create_employee_duplicate_email(self):
        Employee.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            department='Engineering',
            role='Developer'
        )
        data = {
            'name': 'Jane Doe',
            'email': 'john.doe@example.com',
            'department': 'HR',
            'role': 'Manager'
        }
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_create_employee_empty_name(self):
        data = {
            'name': '',
            'email': 'test@example.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_create_employee_invalid_email(self):
        data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'department': 'Engineering',
            'role': 'Developer'
        }
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        Employee.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            department='HR',
            role='Manager'
        )
        
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_list_employees_pagination(self):
        for i in range(15):
            Employee.objects.create(
                name=f'Employee {i}',
                email=f'employee{i}@example.com',
                department='Engineering',
                role='Developer'
            )
        
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)
        self.assertIsNotNone(response.data['next'])

    def test_list_employees_filter_by_department(self):
        Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        Employee.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            department='HR',
            role='Manager'
        )
        
        response = self.client.get('/api/employees/?department=Engineering')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['department'], 'Engineering')

    def test_list_employees_filter_by_role(self):
        Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        Employee.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            department='Engineering',
            role='Manager'
        )
        
        response = self.client.get('/api/employees/?role=Developer')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['role'], 'Developer')

    def test_retrieve_employee_success(self):
        employee = Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        
        response = self.client.get(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')
        self.assertEqual(response.data['email'], 'john@example.com')

    def test_retrieve_employee_not_found(self):
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee_success(self):
        employee = Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        
        data = {
            'name': 'John Updated',
            'email': 'john.updated@example.com',
            'department': 'Sales',
            'role': 'Manager'
        }
        response = self.client.put(f'/api/employees/{employee.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        employee.refresh_from_db()
        self.assertEqual(employee.name, 'John Updated')
        self.assertEqual(employee.department, 'Sales')

    def test_update_employee_not_found(self):
        data = {
            'name': 'John Updated',
            'email': 'john@example.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        response = self.client.put('/api/employees/999/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee_success(self):
        employee = Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            department='Engineering',
            role='Developer'
        )
        
        response = self.client.delete(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_delete_employee_not_found(self):
        response = self.client.delete('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authentication_required(self):
        self.client.credentials()
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_employee_date_joined_auto_generated(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('date_joined', response.data)
        self.assertEqual(response.data['date_joined'], date.today().isoformat())

