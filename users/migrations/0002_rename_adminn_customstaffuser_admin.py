# Generated by Django 3.2.23 on 2023-12-20 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customstaffuser',
            old_name='adminn',
            new_name='admin',
        ),
    ]