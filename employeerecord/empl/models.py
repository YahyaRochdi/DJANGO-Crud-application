from email.policy import default
from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
def rand():
    return  User.objects.make_random_password()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="uploads", default='e.png')
    mobile = models.CharField(unique=True, max_length=10)
    email = models.EmailField()
    password = User.objects.make_random_password()
    datetime = models.DateTimeField(auto_now_add=True)   
    CLOUD= 'Cloud'
    DEVOPS = 'DevOps'
    RESEAU = 'Réseau'
    SECURITE = 'Sécurité'
    HR = 'HR'
    FINANCE="Finance"
    OTHER="Autre"
    DEPARTEMENT_TYPE_CHOICES = [
        (CLOUD, 'Cloud'),
        (DEVOPS, 'Devops'),
        (RESEAU, 'Réseau'),
        (SECURITE, 'Securité'),
        (HR, 'HR'),
        ( FINANCE,'Finance') ,
        ( OTHER,'Other') ]
    Departement=models.CharField(max_length=8,choices=DEPARTEMENT_TYPE_CHOICES,default=OTHER)

    password = models.CharField(max_length=18,)

    
    