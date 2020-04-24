from django.db.models import Q
from django.shortcuts import render
from .serializers import (
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
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin
)


class EmployeeListView(CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyView(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class ProjectListView(CreateModelMixin, ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        qs = Project.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) |
                           Q(description__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        qs = Mentor.objects.all()[0]
        serializer.save(manager=qs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectCreateView(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        qs = Mentor.objects.all()[0]
        serializer.save(manager=qs)


class ProjectRetrieveView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDestroyView(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
