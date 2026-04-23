from django.urls import path
from .views import home, employee_network

urlpatterns = [
    path('', home, name = 'home'),
    path('employee/', employee_network, name='employee_network')
]