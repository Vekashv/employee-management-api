from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    department = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']
        db_table = 'employees'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.name} ({self.email})"

    def clean(self):
        if not self.name or not self.name.strip():
            raise ValidationError({'name': 'Name cannot be empty.'})
        
        if self.email:
            self.email = self.email.lower().strip()
        
        if self.pk:
            if Employee.objects.filter(email=self.email).exclude(pk=self.pk).exists():
                raise ValidationError({'email': 'An employee with this email already exists.'})
        else:
            if Employee.objects.filter(email=self.email).exists():
                raise ValidationError({'email': 'An employee with this email already exists.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

