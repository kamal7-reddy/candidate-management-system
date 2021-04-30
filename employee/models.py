from django.db import models

# Create your models here.
class Employee_data(models.Model):
    
    full_name     = models.CharField(max_length = 50)
    gender        = models.CharField(max_length = 10)
    phone_no      = models.CharField(max_length = 20)
    alternate_no  = models.CharField(max_length = 20)
    email_id      = models.EmailField(max_length = 50)
    date_of_birth = models.DateField(auto_now_add=False)

    year_of_exp   = models.IntegerField(default = True)
    job_position  = models.CharField(max_length = 50)
    current_ctc   = models.IntegerField(default = True)
    expected_ctc  = models.IntegerField(default = True)
    current_company = models.CharField(max_length = 100)
    

    skill_set               = models.CharField(max_length = 200)
    work_Location           = models.CharField(max_length = 20)
    preferred_location      = models.CharField(max_length = 15)
    negotiable              = models.CharField(max_length = 10)
    currently_serving       = models.CharField(max_length = 10)
    in_days                 = models.CharField(max_length = 10)
    application_date        = models.DateField(auto_now_add=True)
    reason_for_job_change   = models.CharField(max_length = 100)
    status                  = models.CharField(max_length = 30)
    document                = models.FileField(upload_to='documents/')
    
