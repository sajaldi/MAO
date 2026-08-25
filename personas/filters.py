import django_filters
from .models import Company, Person


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['name', 'email']


class PersonFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    position = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    company_name = django_filters.CharFilter(field_name='company__name', lookup_expr='icontains')
    hire_date_from = django_filters.DateFilter(field_name='hire_date', lookup_expr='gte')
    hire_date_to = django_filters.DateFilter(field_name='hire_date', lookup_expr='lte')
    created_at_from = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Person
        fields = [
            'first_name', 'last_name', 'email', 'position',
            'company', 'company_name', 'hire_date_from', 'hire_date_to',
            'created_at_from', 'created_at_to'
        ]