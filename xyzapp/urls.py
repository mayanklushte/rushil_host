from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    #admin 
    path('dashboard',views.homepage,name='index'), #Index Page
    path('view_sales',views.view_sales,name='view_sales'), # Sales Data View Page
    path('charts',views.chartpage,name='charts'),# Charts Page View
    path('registration',views.registrationpage,name='registration'), #Registration Page
    path('add_registration_function',views.add_registration_function,name='add_registration_function'), # Registration Function For Add Form Data into Database
    path('view_registration',views.view_registration,name='view_registration'), # Registration Data View
]
