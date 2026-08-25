from rest_framework import serializers
from .models import Company, Person


class CompanySerializer(serializers.ModelSerializer):
    people_count = serializers.IntegerField(source='people.count', read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at', 'people_count']
        read_only_fields = ['created_at', 'updated_at', 'people_count']


class PersonSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        source='company',
        write_only=True
    )
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Person
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'email', 'phone',
            'position', 'company', 'company_id', 'hire_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'full_name']