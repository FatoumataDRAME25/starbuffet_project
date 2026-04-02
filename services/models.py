from django.db import models

# Create your models here.

class Traiteur(models.Model):
    fullname = models.CharField(max_length= 128)
    speciality = models.CharField(max_length=64)
    description = models.TextField()
    adress = models.CharField(max_length=128)
    is_actif = models.BooleanField(default = False)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add= True)
    phone = models.CharField(max_length=128)

 
    def __str__(self):
        return f" Bienvenue {self.fullname}"