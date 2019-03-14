from django.urls import path
from .views import QuestionsView, QuestionsDetailsView

urlpatterns = [
    path('', QuestionsView.as_view(), name="create_question"),
    path('<int:pk>', QuestionsDetailsView.as_view(), name="question_details")
]
