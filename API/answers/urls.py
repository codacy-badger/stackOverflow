from django.urls import path
from .views import AnswersView

urlpatterns = [
    path('', AnswersView.as_view(), name="create"),
]