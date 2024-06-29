from django.db import models

# Create your models here.
import uuid

class Doc(models.Model):
    id = models.CharField (max_length=500, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=500)
    semestre = models.IntegerField()
    


    def __str__(self):
        return self.name
