# Generated by Django 4.2.7 on 2023-12-01 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salama', '0013_alter_orderform_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderform',
            options={'ordering': ['item', 'description', 'quantity', 'route']},
        ),
        migrations.RemoveField(
            model_name='orderform',
            name='user',
        ),
    ]