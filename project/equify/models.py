from django.db import models

class UserInput(models.Model):
    age = models.IntegerField()
    education_qualification = models.CharField(max_length=100)
    years_of_experience = models.FloatField()
    current_salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10)
