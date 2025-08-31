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

class JobPost(models.Model):
    job_poasted_by = models.ForeignKey(Scout, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_salary = models.DecimalField(max_digits=10, decimal_places=2)
    