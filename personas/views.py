from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Company, Person
from .serializers import CompanySerializer, PersonSerializer
from .filters import CompanyFilter, PersonFilter


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CompanyFilter
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.select_related('company').all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PersonFilter
    search_fields = ['first_name', 'last_name', 'email', 'position']
    ordering_fields = ['last_name', 'first_name', 'email', 'position', 'hire_date', 'created_at']
    ordering = ['last_name', 'first_name']

    @action(detail=False, methods=['get'])
    def by_company(self, request):
        company_id = request.query_params.get('company_id')
        if not company_id:
            return Response({'error': 'company_id parameter required'}, status=400)
        people = self.queryset.filter(company_id=company_id)
        serializer = self.get_serializer(people, many=True)
        return Response(serializer.data)


class CompanyListView(ListView):
    model = Company
    template_name = 'personas/company_list.html'
    context_object_name = 'page_obj'
    paginate_by = 20

    def get_queryset(self):
        queryset = Company.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'personas/company_form.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        messages.success(self.request, 'Empresa creada correctamente.')
        return super().form_valid(form)


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'personas/company_form.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        messages.success(self.request, 'Empresa actualizada correctamente.')
        return super().form_valid(form)


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'personas/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.people.exists():
            messages.error(request, 'No se puede eliminar la empresa porque tiene personas asociadas.')
            return self.get(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Empresa eliminada correctamente.')
        return super().form_valid(form)


class PersonListView(ListView):
    model = Person
    template_name = 'personas/person_list.html'
    context_object_name = 'page_obj'
    paginate_by = 20

    def get_queryset(self):
        queryset = Person.objects.select_related('company').all()
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')
        email = self.request.GET.get('email')
        company = self.request.GET.get('company')

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if company:
            queryset = queryset.filter(company_id=company)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context


class PersonCreateView(CreateView):
    model = Person
    template_name = 'personas/person_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'position', 'company', 'hire_date']
    success_url = reverse_lazy('person_list')

    def form_valid(self, form):
        messages.success(self.request, 'Persona creada correctamente.')
        return super().form_valid(form)


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'personas/person_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'position', 'company', 'hire_date']
    success_url = reverse_lazy('person_list')

    def form_valid(self, form):
        messages.success(self.request, 'Persona actualizada correctamente.')
        return super().form_valid(form)


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'personas/person_confirm_delete.html'
    success_url = reverse_lazy('person_list')

    def form_valid(self, form):
        messages.success(self.request, 'Persona eliminada correctamente.')
        return super().form_valid(form)