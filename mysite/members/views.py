from django.shortcuts import render
from members.models import Member
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from IPython import embed

from members.forms import MemberForm

from django.contrib.auth.decorators import login_required

#from django.contrib.auth import logout


# Create your views here.

def member(request,member_id):
    member = Member.objects.get(id=member_id)
    
    context={"member": member}
    
    response = render(request,'members/member_detail.html', context )
  
    return response



def member_list(request):
    
    member_list = Member.objects.all()        
    context={"member_list": member_list}
    response = render(request,'members/member_list.html', context )
    
    return response

@login_required
def member_update(request,member_id):
    member = Member.objects.get(id=member_id)
    # Here I check if the logged in user is the owner of the information.
    if member.user!=request.user:
        #message='You do not have permission to change this information!'
        #return render(request,'members/no_access.html', {'message':message} )
        return HttpResponseRedirect(reverse('no_access'))
    
    if request.method=="POST":
        form = MemberForm(request.POST, instance=member) # populates the form fields with POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_profile',kwargs={'member_id':member_id}))
        else:
            return HttpResponseRedirect('/')

    form = MemberForm(instance=member)
    return render(request,'members/member_update.html',{'form':form})

def no_access(request):
    message='You do not have permission to access this page!'
    context={'message':message}
    response = render(request,'members/no_access.html', context )
    
    return response

#def logout_view(request):
    #D={}
    #if request.user.is_authenticated:
     #   D['reply']='Success, You have logged out!'
    #else:
     #   D['reply']='You were not logged in!'
    #logout(request)
    #return render(request,'members/mylogout.html', {} )
