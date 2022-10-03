from rest_framework.views import APIView
from .serializers import PollSerializer
from .models import Poll, Vote, Choise
from rest_framework import generics
from .paginations import PollPanination

class PollList(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    
class PollDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    pagination_class = PollPanination
    
