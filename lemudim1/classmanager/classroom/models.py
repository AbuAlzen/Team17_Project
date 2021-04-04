from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   name = models.CharField(max_length=50)#
   email = models.EmailField(max_length=50)
   subject = models.CharField(max_length=50)
   Age = models.CharField(max_length=10)
   per_hour = models.CharField(max_length=50)

   def __str__(self):
       return self.name