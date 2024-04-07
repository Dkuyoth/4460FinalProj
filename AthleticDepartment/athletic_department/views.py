from django.shortcuts import render
from .models import Team, Employee, Athlete, Equipment, Event, Income


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})
