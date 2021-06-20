from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.name


class Candidates(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)
    company=models.ManyToManyField(Company,blank=True)
    def __str__(self):
        return self.name
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name
    

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100 , blank=True)
    option_four = models.CharField(max_length=100 , blank=True)
    
    marks = models.IntegerField(default=5)
    
    def __str__(self):
        return self.question
    
    
class ScoreBoard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()        