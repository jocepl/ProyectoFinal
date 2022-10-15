from django.db import models

# Create your models here.

class investigations(models.Model):

    def __str__(self):
        return f'{self.investigation_owner} creó {self.investigation_name}'

    domain_name = models.CharField(max_length=40)
    investigation_owner = models.CharField(max_length=40)
    investigation_name = models.CharField(max_length=40)
    investigation_date = models.DateField()
    investigation_overview = models.CharField(max_length= 500)
    # investigation_media = 

class bugs(models.Model):

    def __str__(self):
        return f'{self.bugs_owner} creó {self.bugs_name}'

    bugs_domain = models.CharField(max_length= 20)
    bugs_date = models.DateField()
    bugs_owner = models.CharField(max_length= 40)
    bugs_name = models.CharField(max_length=40)
    bugs_description = models.CharField(max_length= 500)
    bugs_blocking = models.BooleanField(default=False)
    #bugs_media = models.

class tips(models.Model):

    def __str__(self):
        return f'{self.tips_owner} creó {self.tips_name}'

    tips_owner = models.CharField(max_length= 40)
    tips_name = models.CharField(max_length= 250)
    tips_description = models.CharField(max_length= 500)
    tips_date = models.DateField()
    tips_email = models.EmailField()
    #tips_media = 
    tips_link = models.URLField()