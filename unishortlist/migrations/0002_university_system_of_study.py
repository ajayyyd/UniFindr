# Generated by Django 5.1.6 on 2025-03-20 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unishortlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='system_of_study',
            field=models.CharField(default='offline', max_length=50),
        ),
    ]
