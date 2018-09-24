from django.db import models


class Citizen(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
        )
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    dob = models.DateField('Date of Birth')
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    citizenship_no = models.CharField(max_length=20)
    issue_date = models.DateField()
    issue_district = models.CharField(max_length=25)
    
