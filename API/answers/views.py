from django.shortcuts import render
from rest_framework import generics
from .serializers import AnswersSerializer
from .models import Answer


# Create your views here.
class AnswersView(generics.ListCreateAPIView):
    serializer_class = AnswersSerializer
    queryset = Answer.objects.all()
