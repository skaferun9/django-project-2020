# Generated by Django 3.0.2 on 2020-03-07 04:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainshop', '0002_auto_20200307_0428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ticket_Picnic',
            new_name='Ticket',
        ),
    ]
