from django.db import models

# Create your models here.
class Team(models.Model):
    team_name=models.CharField(max_length=50)
    team_country=models.CharField(max_length=50)
    home_colour=models.CharField(max_length=50)
