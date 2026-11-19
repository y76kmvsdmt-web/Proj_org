from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('location/', views.location, name='location'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
        # Сотрудники
    path('data/employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('data/employees/add/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('data/employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('data/employees/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('data/employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Заказчики
    path('data/customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('data/customers/add/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('data/customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('data/customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('data/customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # Проекты
    path('data/projects/', views.ProjectListView.as_view(), name='project_list'),
    path('data/projects/add/', views.ProjectCreateView.as_view(), name='project_create'),
    path('data/projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('data/projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('data/projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # Договоры
    path('data/contracts/', views.ContractListView.as_view(), name='contract_list'),
    path('data/contracts/add/', views.ContractCreateView.as_view(), name='contract_create'),
    path('data/contracts/<int:pk>/', views.ContractDetailView.as_view(), name='contract_detail'),
    path('data/contracts/<int:pk>/edit/', views.ContractUpdateView.as_view(), name='contract_update'),
    path('data/contracts/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),

    # Оборудование
    path('data/equipment/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('data/equipment/add/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('data/equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('data/equipment/<int:pk>/edit/', views.EquipmentUpdateView.as_view(), name='equipment_update'),
    path('data/equipment/<int:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipment_delete'),
]
