# Generated by Django 4.2.7 on 2023-11-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salama', '0009_alter_orderform_item_alter_orderform_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderform',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]