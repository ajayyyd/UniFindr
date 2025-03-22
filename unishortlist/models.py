

# Create your models here.
from django.db import models

class UserData(models.Model):
    country = models.CharField(max_length=50)
    system_of_study = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    intake = models.CharField(max_length=20)
    level= models.CharField(max_length=20)
    lang_test = models.CharField(max_length=50)
    test_score = models.FloatField()
    marks_10th = models.FloatField()
    marks_12th = models.FloatField()
    CGPA = models.FloatField()


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    course = models.CharField(max_length=255)
    system_of_study = models.CharField(max_length=50,default="offline")
    intake = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    accepted_lt = models.CharField(max_length=255)
    lt_score = models.FloatField()
    min_marks = models.FloatField()
    min_CGPA = models.FloatField()
    fees = models.FloatField()


