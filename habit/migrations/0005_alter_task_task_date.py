# Generated by Django 4.0.5 on 2022-06-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_alter_habitmodel_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(),
        ),
    ]
