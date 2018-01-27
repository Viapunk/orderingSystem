# Generated by Django 2.0.1 on 2018-01-25 20:11

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20180125_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assignee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Person'),
        ),
        migrations.AlterField(
            model_name='order',
            name='productList',
            field=jsonfield.fields.JSONField(),
        ),
    ]