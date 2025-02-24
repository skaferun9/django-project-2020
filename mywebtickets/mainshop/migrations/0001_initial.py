# Generated by Django 3.0.2 on 2020-03-07 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('even_date', models.DateTimeField(null=True)),
                ('event_time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('ticket_price', models.FloatField(blank=True, default=None, null=True)),
                ('ticket_amount', models.IntegerField(blank=True, default=None, null=True)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('is_popular', models.BooleanField(null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainshop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Picnic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainshop.Event')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
