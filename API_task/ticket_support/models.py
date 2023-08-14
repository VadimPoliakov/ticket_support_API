from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.ForeignKey(Status, related_name='tickets', on_delete=models.PROTECT)
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
