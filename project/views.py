from django.shortcuts import render
from project.serializers import (
    ProjectSerializer, EmployeeSerializer, MentorSerializer)
from project.models import (Project, Employee, Mentor)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView)
# Create your views here.


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyView(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
