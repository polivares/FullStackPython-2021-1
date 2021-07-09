from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Course(models.Model):
    cod_course = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    max_students = models.IntegerField()
    #n_enrolled (?)
    students =  models.ManyToManyField(Student, related_name="courses")


