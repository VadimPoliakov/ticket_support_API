from django.contrib import admin

# Register your models here.
from .models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'subject',)
    search_fields = ('id', 'subject',)
    list_editable = ('status',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'ticket',)
    search_fields = ('id', 'ticket')


# class StatusAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     list_display_links = ('name',)
#     search_fields = ('name',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Message, MessageAdmin)
#admin.site.register(Status, StatusAdmin)
