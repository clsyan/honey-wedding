# Generated by Django 3.1.2 on 2020-10-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='is_confirmed',
            new_name='is_approved',
        ),
    ]
