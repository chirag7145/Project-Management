from django.urls import path, include
from .views import EmployeeListView, EmployeeCreateView, EmployeeRetrieveView, EmployeeDestroyView, ProjectListView, ProjectCreateView, ProjectRetrieveView, ProjectDestroyView

urlpatterns = [
    path('employees/', EmployeeListView.as_view()),
    path('employees/create/', EmployeeCreateView.as_view()),
    path('employees/delete/<int:pk>', EmployeeDestroyView.as_view()),
    path('employees/detail/<int:pk>', EmployeeRetrieveView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('projects/create/', ProjectCreateView.as_view()),
    path('projects/delete/<int:pk>', ProjectDestroyView.as_view()),
    path('projects/detail/<int:pk>', ProjectRetrieveView.as_view()),
]
