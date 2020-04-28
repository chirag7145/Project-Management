from django.contrib import admin

# Register your models here.
from project.models import (User, Project, Employee, Mentor)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_employee', 'is_mentor')
    # list_editable = ('is_employee', 'is_mentor',)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email',)

    def get_email(self, obj):
        return obj.user.email


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)
