from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def location(request):
    return render(request, 'main/location.html')

def projects(request):
    return render(request, 'main/projects.html')

def services(request):
    return render(request, 'main/services.html')

class ToDetailMixin:
    """После редактирования возвращает на страницу деталей записи."""
    detail_url = None

    def get_success_url(self):
        return reverse(self.detail_url, args=[self.object.pk])


# ---------- Сотрудники ----------
class EmployeeListView(ListView):
    model = Employee
    template_name = 'main/employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'main/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('employee_list')
    extra_context = {'title': 'Добавление сотрудника'}

class EmployeeUpdateView(ToDetailMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('employee_list')
    detail_url = 'employee_detail'
    extra_context = {'title': 'Редактирование сотрудника'}

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'main/crud_confirm_delete.html'
    success_url = reverse_lazy('employee_list')


# ---------- Заказчики ----------
class CustomerListView(ListView):
    model = Customer
    template_name = 'main/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'main/customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('customer_list')
    extra_context = {'title': 'Добавление заказчика'}

class CustomerUpdateView(ToDetailMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('customer_list')
    detail_url = 'customer_detail'
    extra_context = {'title': 'Редактирование заказчика'}

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'main/crud_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


# ---------- Проекты ----------
class ProjectListView(ListView):
    model = Project
    template_name = 'main/project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'main/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('project_list')
    extra_context = {'title': 'Добавление проекта'}

class ProjectUpdateView(ToDetailMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('project_list')
    detail_url = 'project_detail'
    extra_context = {'title': 'Редактирование проекта'}

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'main/crud_confirm_delete.html'
    success_url = reverse_lazy('project_list')


# ---------- Договоры ----------
class ContractListView(ListView):
    model = Contract
    template_name = 'main/contract_list.html'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'main/contract_detail.html'

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('contract_list')
    extra_context = {'title': 'Добавление договора'}

class ContractUpdateView(ToDetailMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('contract_list')
    detail_url = 'contract_detail'
    extra_context = {'title': 'Редактирование договора'}

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'main/crud_confirm_delete.html'
    success_url = reverse_lazy('contract_list')


# ---------- Оборудование ----------
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'main/equipment_list.html'

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'main/equipment_detail.html'

class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('equipment_list')
    extra_context = {'title': 'Добавление оборудования'}

class EquipmentUpdateView(ToDetailMixin, UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'main/crud_form.html'
    success_url = reverse_lazy('equipment_list')
    detail_url = 'equipment_detail'
    extra_context = {'title': 'Редактирование оборудования'}

class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'main/crud_confirm_delete.html'
    success_url = reverse_lazy('equipment_list')