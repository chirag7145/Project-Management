from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undisclosed'),
    )

    is_employee = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER, default='u')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("getUser", kwargs={"username": self.username})


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField('Project')

    def __str__(self):
        return self.user.username


class Mentor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    manager = models.ForeignKey(
        Mentor, verbose_name="Project Manager", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("getproject", kwargs={"title": self.title})
