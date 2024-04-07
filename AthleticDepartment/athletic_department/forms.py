from django import forms
from .models import Team, Employee, Athlete, Equipment, Event, Income


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'sport_type']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'team']

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'scholarship_amount', 'team']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'cost', 'team']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'income', 'expense', 'team']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['type', 'amount', 'date', 'team']        

