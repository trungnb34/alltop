from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PollSerializer
from django.shortcuts import get_object_or_404
from .models import Poll
from rest_framework import generics

class PollList(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    # def get(self, request):
    #     polls = Poll.objects.all()[:20]
    #     pollSerializers = PollSerializer(polls, many=True)
    #     return Response(pollSerializers.data, status=200)
    
class PollDetail(generics.RetrieveDestroyAPIView):
    # def get(self, request, pk):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     # print("poll : ", poll)
    #     pollSerializer = PollSerializer(poll)
    #     return Response(pollSerializer.data, status=200)
    serializer_class = PollSerializer
    queryset = Poll.objects.all()