from django.db import models


class Student(models.Model):
    #id
    id = models.AutoField(primary_key=True)
    #login
    login = models.CharField(max_length=64)
    #password
    pswrd = models.CharField(max_length=64)
    #Name
    name = models.CharField(max_length=64)
    #Phone number
    phone = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # login
    login = models.CharField(max_length=64)
    # password
    pswrd = models.CharField(max_length=64)
    # Name
    name = models.CharField(max_length=64)
    # Phone number
    phone = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    #id
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    #Date
    date_time = models.DateTimeField()
