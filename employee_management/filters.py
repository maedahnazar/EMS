import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.NumberFilter(lookup_expr='exact')
    salary_lte = django_filters.NumberFilter(field_name='salary', lookup_expr='lte', label='Salary ≤')
    salary_gte = django_filters.NumberFilter(field_name='salary', lookup_expr='gte', label='Salary ≥')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='exact', label='Salary =')

    class Meta:
        model = Employee
        fields = ['department', 'salary', 'salary_lte', 'salary_gte']
