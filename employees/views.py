from rest_framework import status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'department', 'role']
    ordering_fields = ['name', 'email', 'date_joined', 'department', 'role']
    ordering = ['-date_joined']

    def get_queryset(self):
        queryset = Employee.objects.all()
        
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')
        
        if department:
            queryset = queryset.filter(department__iexact=department)
        if role:
            queryset = queryset.filter(role__iexact=role)
        
        return queryset


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    lookup_field = 'id'

