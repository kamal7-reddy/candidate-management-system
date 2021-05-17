from django.urls import path
from . import views

urlpatterns = [
    path('',views.login , name = 'login') , 
    path('logout',views.logout , name = 'logout') ,
    path('home', views.home , name = 'home'),
    path('employee', views.employee , name = 'employee'),
    path('view_condidate_form/<str:pk>/', views.view_condidate_form , name = 'view_condidate_form'),

    path('update_condidate_form/<str:pk>/', views.update_condidate_form, name = 'update_condidate_form'),
    path('delete_condidate_form/<str:pk>/', views.delete_condidate_form , name = 'delete_condidate_form'),
    path('export_condidate_list', views.export_condidate_list , name = 'export_condidate_list'),
   
  
]  