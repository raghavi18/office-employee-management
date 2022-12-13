from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    empid= models.CharField(max_length=50)
    empdept= models.CharField(max_length=100,null=True)
    designation= models.CharField(max_length=100,null=True)
    contact= models.CharField(max_length=15,null=True)
    gender= models.CharField(max_length=50,null=True)
    joiningdate= models.DateField(null=True)
    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company1name= models.CharField(max_length=100,null=True)
    company1desig= models.CharField(max_length=100,null=True)
    company1salary= models.CharField(max_length=100,null=True)
    company1duration= models.CharField(max_length=100,null=True)
    company2name= models.CharField(max_length=100,null=True)
    company2desig= models.CharField(max_length=100,null=True)
    company2salary= models.CharField(max_length=100,null=True)
    company2duration= models.CharField(max_length=100,null=True)
    company3name= models.CharField(max_length=100,null=True)
    company3desig= models.CharField(max_length=100,null=True)
    company3salary= models.CharField(max_length=100,null=True)
    company3duration= models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username