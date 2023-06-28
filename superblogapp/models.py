
from django.db import models


# Create your models here.
class Sigin(models.Model):
    #username=models.CharField(max_length=20)
    
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    cnfrm_pwd=models.CharField(max_length=10)

    # groups = models.ManyToManyField('auth.Group', related_name='sigin_groups')
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='sigin_user_permissions')
