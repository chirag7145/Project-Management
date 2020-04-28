from django.shortcuts import render, get_object_or_404, redirect
from project.models import User, Mentor, Project, Employee


def AllUsers(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users/allUsers.html', context)


def GetUser(request, username):
    user = get_object_or_404(User, username=username)

    if user:
        projects_assigned = []
        projects_mentoring = []
        if user.is_employee:
            projects_assigned = Employee.objects.get(user=user).projects.all()
        if user.is_mentor:
            projects_mentoring = Mentor.objects.get(
                user=user).project_set.all()
        context = {
            'username': user.username,
            'email': user.email,
            'is_mentor': user.is_mentor,
            'is_employee': user.is_employee,
            'projects_assigned': projects_assigned,
            'projects_mentoring': projects_mentoring,
        }
        return render(request, 'users/getUser.html', context)


def AllProjects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/allProject.html', context)


def GetProject(request, title):
    project = get_object_or_404(Project, title=title)
    context = {
        'title': project.title,
        'description': project.description,
        'manager': project.manager,
        'employees': project.employee_set.all()
    }
    return render(request, 'projects/getProject.html', context)
