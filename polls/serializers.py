from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Poll, Choise, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

class ChoiseSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choise
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    choises = ChoiseSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = "__all__"
        
