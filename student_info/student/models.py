from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField()
    city=models.CharField()
    def __str__(self):
        return self.name
