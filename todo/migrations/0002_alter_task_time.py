# Generated by Django 5.0.1 on 2024-01-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True, error_messages='good', null=True),
        ),
    ]
