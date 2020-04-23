from django.urls import path, include
from project.views import EmployeeListView, EmployeeCreateView, EmployeeRetrieveView, EmployeeDestroyView

urlpatterns = [
    path('employees/', EmployeeListView.as_view()),
    path('employees/create/', EmployeeCreateView.as_view()),
    path('employees/delete/<int:pk>', EmployeeDestroyView.as_view()),
    path('employees/detail/<int:pk>', EmployeeRetrieveView.as_view()),
]
