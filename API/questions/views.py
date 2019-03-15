from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionsSerializer


# Create your views here.
class QuestionsView(generics.ListCreateAPIView):
    serializer_class = QuestionsSerializer
    queryset = Question.objects.all()


class QuestionsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsSerializer
    queryset = Question.objects.all()
