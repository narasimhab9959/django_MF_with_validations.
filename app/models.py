from django.db import models
from django import forms
# Create your models here.


def Check_of_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('name Error')

def length_of_n(name):
    if len(name)<=5:
        raise forms.ValidationError('length of name error')

class Topic(models.Model):
    topic_name=models.CharField(max_length=100)


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[Check_of_a,length_of_n])
    url=models.URLField()


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    
