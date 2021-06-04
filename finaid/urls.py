from django.urls import path
from .views import finaidList, finaidDetailView

urlpatterns = [
    path("", finaidList.as_view()),
    path("<int:id>", finaidDetailView.as_view()),
]