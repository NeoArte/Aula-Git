# Generated by Django 3.2.6 on 2021-08-19 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cateforia',
            new_name='categoria',
        ),
    ]
