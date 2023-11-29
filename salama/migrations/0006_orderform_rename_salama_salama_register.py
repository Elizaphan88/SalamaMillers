# Generated by Django 4.2.7 on 2023-11-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salama', '0005_rename_email_salama_email_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('route', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.RenameModel(
            old_name='salama',
            new_name='salama_register',
        ),
    ]
