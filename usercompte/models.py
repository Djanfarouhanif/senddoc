from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid

user = User()

class Student(models.Model):
    id = models.CharField(max_length=500, default=uuid.uuid4, primary_key = True)
    user = models.ForeignKey(user, on_delete= models.CASCADE)
    departemment = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username