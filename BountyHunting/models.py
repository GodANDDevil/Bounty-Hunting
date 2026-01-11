from django.db import models

# Create your models here.

class Scout(models.Model):
    scout_images = models.FileField(null=True,blank=True,upload_to='scout/images/')
    scout_Company_name = models.CharField(max_length=100)
    scout_gmail = models.EmailField()
    scout_password = models.CharField(max_length=100)
    scout_phone = models.CharField(max_length=15)
    scout_address = models.TextField()
    scout_reg_no = models.CharField(max_length=50)

class Seeker(models.Model):
    seeker_images = models.FileField(null=True,blank=True,upload_to='seeker/images/')
    seeker_Full_name = models.CharField(max_length=100)
    seeker_gmail = models.EmailField()
    seeker_password = models.CharField(max_length=100)
    seeker_phone = models.CharField(max_length=15)
    seeker_address = models.TextField()
    seeker_citi_no = models.CharField(max_length=50)
    seeker_dof = models.DateField()

class SeekerProfile(models.Model):
    seeker_profile = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    seeker_see = models.FileField(null=True,blank=True,upload_to='seeker/see/')
    seeker_highschool = models.FileField(null=True,blank=True,upload_to='seeker/highschool/')
    seeker_bachelor = models.FileField(null=True,blank=True,upload_to='seeker/bachelor/')
    seeker_master = models.FileField(null=True,blank=True,upload_to='seeker/master/')
    seeker_phd = models.FileField(null=True,blank=True,upload_to='seeker/phd/')

class JobPost(models.Model):
    job_poasted_by = models.ForeignKey(Scout, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_salary = models.DecimalField(max_digits=10, decimal_places=2) 
    job_imges = models.FileField(null=True,blank=True,upload_to='jobpost/images/')
    
class Index_Seeker_Images(models.Model):
    index_seeker_img = models.FileField(null=True,blank=True,upload_to='index/seeker/')

class Index_Scout_Images(models.Model):
    index_scout_img = models.FileField(null=True,blank=True,upload_to='index/scout/')

class Ads_Images(models.Model):
    ads_img = models.FileField(null=True,blank=True,upload_to='ads/')

class Login_Images(models.Model):
    login_img = models.FileField(null=True,blank=True,upload_to='login/')

class Register_Images(models.Model):
    register_img = models.FileField(null=True,blank=True,upload_to='register/')