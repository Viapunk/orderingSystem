# Generated by Django 2.0.1 on 2018-01-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180120_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='someurl', max_length=1000),
        ),
    ]