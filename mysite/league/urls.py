from django.urls import path
from . import views

urlpatterns = [
    path('team/id/<int:team_id>', views.team, name="team_profile"),
    path('team_list', views.team_list, name="team_list"),
]