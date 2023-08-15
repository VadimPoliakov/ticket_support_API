from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content']


class TicketViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'subject', 'description', 'status']


class TicketDetailViewSerializer(serializers.ModelSerializer):
    replies = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'user', 'subject', 'description', 'status', 'replies']


class TicketChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'status']


class TicketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.HiddenField(default=Ticket.Status.STATUS_OPEN)

    class Meta:
        model = Ticket
        fields = ['user', 'subject', 'description', 'status']
