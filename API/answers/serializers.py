from rest_framework import serializers
from .models import Answer


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
