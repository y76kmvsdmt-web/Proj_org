from django import forms
from .models import *


def date_widget():
    # type="date" даёт календарь, format нужен, чтобы дата подставлялась при редактировании
    return forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'birth_date': date_widget(),
            'hire_date': date_widget(),
            'characteristic': forms.Textarea(attrs={'rows': 3}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {'address': forms.Textarea(attrs={'rows': 3})}


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'start_date': date_widget(),
            'end_plan_date': date_widget(),
            'end_fact_date': date_widget(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'sign_date': date_widget(),
            'expire_date': date_widget(),
            'projects': forms.CheckboxSelectMultiple(),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {'receipt_date': date_widget()}