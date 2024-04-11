from django.shortcuts import render,redirect
from django.views import View
from .models import Team, Employee, Athlete, Equipment, Event, Income
from .forms import TeamForm, EmployeeForm, AthleteForm, EquipmentForm, EventForm, IncomeForm


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})