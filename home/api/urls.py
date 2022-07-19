from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list_api_view),
    path('employee-list/', views.employee_list_api_view)
]