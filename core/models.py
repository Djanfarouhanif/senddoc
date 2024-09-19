from django.db import models
from django.auth.models import User
# Create your models here.
import uuid
user = User()
#Creation studend table
class Student(models.Model):
    id = models.CharField(max_length=500, default=uuid.uuid4, primary_key = True)
    user = models.ForeignKey(user, on_delete= models.CASCADE)
    departemment = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
#cree une class pour la creation des groupes de travaille


    
class Faculte(models.Model):
    id = models.CharField (max_length=500, default=uuid.uuid4, primary_key=True)
    faculte = models.CharField(max_length=500, default="")
    departement = models.CharField(max_length=500)
    ue = models.CharField(max_length=500)
    semestre = models.IntegerField()
    credit = models.IntegerField()
    file = models.FileField(upload_to='document', unique=True)
    
    def __str__(self):
        return self.departement

