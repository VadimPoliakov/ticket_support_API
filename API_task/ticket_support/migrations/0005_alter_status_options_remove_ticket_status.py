# Generated by Django 4.2.4 on 2023-08-14 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_support', '0004_status_alter_message_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('name',), 'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='status',
        ),
    ]
