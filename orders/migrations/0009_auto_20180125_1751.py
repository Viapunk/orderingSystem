# Generated by Django 2.0.1 on 2018-01-25 17:51

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180124_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='productList',
            field=django_mysql.models.JSONField(default=''),
        ),
    ]
