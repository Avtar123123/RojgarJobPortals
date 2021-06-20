from django.db import models
#from __future__ import unicode_literals  
  
  
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    class Meta:  
        db_table = "student"  
    def __str__(self):
        return self.first_name

# Create your models here.
