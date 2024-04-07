from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100)
    established_date = models.DateField()

    # Add other fields as necessary

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Add other fields as necessary

class Athlete(models.Model):
    athlete_name = models.CharField(max_length=100)
    scholarship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Add other fields as necessary

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Add other fields as necessary

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Add other fields as necessary

class Income(models.Model):
    TYPE_CHOICES = [
        ('donation', 'Donation'),
        ('state', 'State Funding'),
        ('university', 'University Funding'),
        ('tv_network', 'TV Network Payout'),
        ('event_payout', 'Event Payout'),
        # Add more income types as needed
    ]

    income_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class Rank(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.IntegerField()
    record = models.IntegerField()
    
# Remember to run migrations after defining your models
