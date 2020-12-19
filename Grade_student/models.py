from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=200)

    def __str__(self):
        return self.g_name



class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    g = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
