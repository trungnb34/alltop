from django.test import TestCase

# Create your tests here.
from .serializers import PollSerializer

pollSerializer = PollSerializer(data={"question": "The install worked successfully", "created_by": 1})

print(pollSerializer.is_valid())

poll = pollSerializer.save()

print(poll.pk)
