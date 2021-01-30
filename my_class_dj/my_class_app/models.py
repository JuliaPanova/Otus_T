from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=64)
    degree = models.CharField(max_length=64)
    rate = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    #Date
    date_time = models.DateTimeField()
