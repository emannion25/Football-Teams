from django.urls import path
from . import views

urlpatterns = [
    path('member/id/<int:member_id>', views.member, name="member_profile"),
    path('member_list', views.member_list, name="member_list"),
    path('member/update/id/<int:member_id>', views.member_update, name="member_update"),
    path('member/no_access', views.no_access, name="no_access"),
    #path('member/logout',views.logout_view,name='logout'),
]