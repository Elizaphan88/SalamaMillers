# Generated by Django 4.2.7 on 2023-11-20 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salama', '0004_alter_salama_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salama',
            old_name='email',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='salama',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='salama',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='salama',
            old_name='mobile',
            new_name='phone_number',
        ),
    ]