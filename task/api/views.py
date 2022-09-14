from unicodedata import name
from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializer import BookSerializer
from rest_framework import permissions

class BookList(ListCreateAPIView):

    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
         return Book.objects.filter(user=self.request.user.id)

class BookDetailView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user.id)
