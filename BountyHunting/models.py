from django.db import models

# Create your models here.

class Scout(models.Model):
    scout_Company_name = models.CharField(max_length=100)
    scout_gmail = models.EmailField()
    scout_password = models.CharField(max_length=100)
    scout_phone = models.CharField(max_length=15)
    scout_address = models.TextField()
    scout_reg_no = models.CharField(max_length=50)

class Seeker(models.Model):
    seeker_Full_name = models.CharField(max_length=100)
    seeker_gmail = models.EmailField()
    seeker_password = models.CharField(max_length=100)
    seeker_phone = models.CharField(max_length=15)
    seeker_address = models.TextField()
    seeker_citi_no = models.CharField(max_length=50)
    seeker_dof = models.DateField()