from django.db import models

# Create your models here.



class Login(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.EmailField (max_length=200)
    
    def get_absolute_url(self):
        return "/ktranslator/%i" % self.id
