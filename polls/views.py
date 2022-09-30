from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import Poll
# Create your views here.

def poll_list(request):
    MAX_LENGTH = 20
    polls = Poll.objects.all()[:MAX_LENGTH]
    data = {"data" : list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def poll_detai(request, pk):
    poll = get_list_or_404(Poll, pk=pk)
    data = {
        "result" : {
            "question" : poll.question,
            "created_by" : poll.created_by.username,
            "pub_date" : poll.pub_date
        }
    }
    return JsonResponse(data)
