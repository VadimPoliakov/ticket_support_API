from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .permissions import *
from .models import *
from .serializers import *


# Чтение всех тикетов
class TicketsList(generics.ListAPIView):
    serializer_class = TicketViewSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()

        return Ticket.objects.filter(user=self.request.user)


# Чтение тикетов по статусу
class TicketsStatusList(generics.ListAPIView):
    serializer_class = TicketViewSerializer

    def get_queryset(self):
        status_name = self.kwargs.get('status')
        if status_name not in dict(Ticket.Status.choices):
            return None
        if self.request.user.is_staff:
            return Ticket.objects.filter(status=status_name)

        return Ticket.objects.filter(user=self.request.user, status=status_name)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset is None:
            return Response({'detail': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Чтение 1 тикета
class TicketDetail(generics.RetrieveAPIView):
    serializer_class = TicketDetailViewSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsOwnerOrAdminOnly,)


# Создание тикета
class CreateTicket(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


# Изменение статуса тикета
class TicketChange(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TicketChangeSerializer
    queryset = Ticket.objects.all()


# Сообщения добавляются в любой тикет несмотря на права
class TicketReply(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        ticket_id = self.kwargs.get('pk')
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if self.request.user.is_staff or ticket.user == self.request.user:
            serializer.save(user=self.request.user, ticket=ticket)
        else:
            raise PermissionDenied("You do not have permission to create a reply for this ticket.")
