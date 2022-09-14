from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)