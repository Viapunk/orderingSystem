# Generated by Django 2.0.1 on 2018-01-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20180125_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='assignee',
        ),
        migrations.AlterField(
            model_name='order',
            name='isAssigned',
            field=models.BooleanField(),
        ),
    ]
