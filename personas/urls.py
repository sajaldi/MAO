from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, PersonViewSet,
    CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView,
    PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView,
)

router = DefaultRouter()
router.register(r'empresas', CompanyViewSet, basename='empresa')
router.register(r'personas', PersonViewSet, basename='persona')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', PersonListView.as_view(), name='person_list'),
    path('personas/nueva/', PersonCreateView.as_view(), name='person_create'),
    path('personas/<int:pk>/editar/', PersonUpdateView.as_view(), name='person_update'),
    path('personas/<int:pk>/eliminar/', PersonDeleteView.as_view(), name='person_delete'),
    path('empresas/', CompanyListView.as_view(), name='company_list'),
    path('empresas/nueva/', CompanyCreateView.as_view(), name='company_create'),
    path('empresas/<int:pk>/editar/', CompanyUpdateView.as_view(), name='company_update'),
    path('empresas/<int:pk>/eliminar/', CompanyDeleteView.as_view(), name='company_delete'),
]
