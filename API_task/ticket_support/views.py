from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions, status, mixins, generics
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .forms import LoginUserForm
from .permissions import IsOwnerOrAdminOnly, IsOwnerTicketOrAdminOnly
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
        status = get_object_or_404(Status, name=status_name)
        if status:
            if self.request.user.is_staff:
                return Ticket.objects.filter(status=status)

            return Ticket.objects.filter(user=self.request.user, status=status)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# Чтение 1 тикета (Готово)
class TicketDetail(generics.RetrieveAPIView):
    serializer_class = TicketDetailViewSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsOwnerOrAdminOnly,)


# Создание тикета (Готово)
class CreateTicket(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


# Изменение статуса тикета
class TicketChange(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TicketChangeSerializer
    queryset = Ticket.objects.all()


# Добавление сообщения
# class TicketReplyViewSet(mixins.CreateModelMixin,
#                          GenericViewSet):
#     serializer_class = MessageSerializer
#
#     # permission_classes = (IsOwnerOrAdminOnly,)
#
#     def create(self, request, *args, **kwargs):
#         ticket_id = request.data.get('ticket')
#         try:
#             ticket = Ticket.objects.get(id=ticket_id)
#
#             if not request.user.is_staff and request.user != ticket.user:
#                 raise PermissionDenied('Permission denied')
#
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save(ticket=ticket, user=request.user)
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         except Ticket.DoesNotExist:
#             raise NotFound('Ticket not found')

# Сообщения добавляются в любой тикет несмотря на права
class TicketReply(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerTicketOrAdminOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "ticket_support/signin.html"
    success_url = reverse_lazy('signin')


def logout_user(request):
    logout(request)
    return redirect('signin')
