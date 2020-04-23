from django.contrib import admin

# Register your models here.
from project.models import (Project, Employee, Mentor, Assign)

admin.site.register([Project, Employee, Mentor, Assign])
