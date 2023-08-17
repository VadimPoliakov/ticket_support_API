from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'subject',)
    search_fields = ('id', 'subject',)
    list_editable = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'ticket',)
    search_fields = ('id', 'ticket')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_active', 'is_staff')
    list_display_links = ('id', 'email', 'username', 'is_active', 'is_staff')
    search_fields = ('id', 'email', 'username', 'is_active', 'is_staff')
