# Generated by Django 4.2.7 on 2023-11-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salama', '0006_orderform_rename_salama_salama_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='last_name',
            field=models.IntegerField(),
        ),
    ]