# Generated by Django 4.0.5 on 2022-06-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_remove_habitmodel_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitmodel',
            name='finish_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='habitmodel',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]