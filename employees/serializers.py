from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'role', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value.strip()

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        
        value = value.lower().strip()
        
        queryset = Employee.objects.filter(email=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("An employee with this email already exists.")
        
        return value

