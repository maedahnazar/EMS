from rest_framework import viewsets, permissions

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .filters import EmployeeFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = EmployeeFilter
