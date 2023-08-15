from django.db import models


class Ticket(models.Model):
    class Status(models.TextChoices):
        STATUS_CLOSED = 'closed', 'Closed'
        STATUS_OPEN = 'open', 'Open'
        STATUS_FROZEN = 'frozen', 'Frozen'

    status = models.CharField(max_length=7, choices=Status.choices, default=Status.STATUS_OPEN)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'


class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    ticket = models.ForeignKey(Ticket, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('ticket',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
