from django.db import models

# Create your models here.
import uuid

class Faculte(models.Model):
    id = models.CharField (max_length=500, default=uuid.uuid4, primary_key=True)
    departement = models.CharField(max_length=500)
    ue = models.CharField(max_length=500)
    semestre = models.IntegerField()
    credit = models.IntegerField()
    file = models.FileField(upload_to='document', unique=True)
    
    def __str__(self):
        return self.departement

