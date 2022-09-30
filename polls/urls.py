from django.urls import path
from .views import poll_list, poll_detai
from .apiviews import PollDetail, PollList

urlpatterns = [
    path("polls/", view=PollList.as_view(), name="poll_list"),
    path("poll/<int:pk>", view=PollDetail.as_view(), name="poll_detail")
]


