import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management.settings')
django.setup()

from django.contrib.auth.models import User

def create_test_user():
    username = 'testuser'
    password = 'testpass123'
    
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists.")
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Password updated for user '{username}'")
    else:
        user = User.objects.create_user(
            username=username,
            password=password,
            email='testuser@example.com'
        )
        print(f"Test user created successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")
    
    print("\nYou can now use these credentials to get a JWT token:")
    print("POST http://127.0.0.1:8000/api/token/")
    print(f'{{"username": "{username}", "password": "{password}"}}')

if __name__ == '__main__':
    create_test_user()

