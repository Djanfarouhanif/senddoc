from django.db import models

# Create your models here.
import uuid

class Doc(models.Model):
    id = models.CharField (max_length=500, default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='document', unique=True)
    semestre = models.IntegerField()

    def __str__(self):
        return self.title


class Image(models.Model):
    username = models.CharField(max_length=100)
    user_image = models.ImageField()

    def __str__(self):
        return self.username