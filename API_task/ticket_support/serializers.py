from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = Message
        fields = ['user', 'ticket', 'content']


class TicketViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['pk', 'user', 'subject', 'description', 'status']

class TicketDetailViewSerializer(serializers.ModelSerializer):

    replies = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['pk', 'user', 'subject', 'description', 'status', 'replies']


class TicketChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['pk','status']


class TicketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.HiddenField(default=Status.objects.get(pk=1))

    class Meta:
        model = Ticket
        fields = ['user', 'subject', 'description', 'status']