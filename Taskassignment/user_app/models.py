from django.db import models

# Create your models here.
class UserModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100,default=False)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    image = models.FileField(upload_to="files")
    is_admin = models.BooleanField(default=False)
    is_approval = models.CharField(max_length=50)                                  


    
