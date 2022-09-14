from dataclasses import fields
from operator import mod
from rest_framework.serializers import ModelSerializer
from .models import *

class BookSerializer(ModelSerializer):
    
    class Meta:
        model = Book
        fields=['id','book_name','user']