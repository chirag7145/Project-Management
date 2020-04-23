from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undisclosed'),
    )

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='u')

    def __str__(self):
        return self.name


class Mentor(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undisclosed'),
    )

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='u')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    manager = models.ForeignKey(
        Mentor, verbose_name="Project Manager", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Assign(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
