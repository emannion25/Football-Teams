from django.shortcuts import render
from django.http import HttpResponse
from league.models import Team

from IPython import embed

# Create your views here.

def team(request,team_id):
    team = Team.objects.get(id=team_id)
    
    #------------------------
    # Use this to change 'problem' colours
    colourlist=team.home_colour.split()
    thecolour=colourlist[0]
    if thecolour=="White" or thecolour=="Black":
        thecolour="Grey"
    elif thecolour=="Light":
        thecolour="Lightblue"
    #------------------------
    
    context={"team": team, "thecolour":thecolour}
    
    response = render(request,'league/team_detail.html', context )
  
    return response



def team_list(request):
    
    team_list = Team.objects.all()        
    context={"team_list": team_list}
    response = render(request,'league/team_list.html', context )
    
    return response

def home(request):
    context={}
    if request.user.is_authenticated:
        name=request.user.username
        context['name']=name
    else:
        context['name']=''
    response = render(request,'league/home.html', context )
    
    return response


