# Generated by Django 5.0.6 on 2024-06-13 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_sugessted_by_relationmodel_suggested_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmodel',
            name='receiver',
        ),
    ]
