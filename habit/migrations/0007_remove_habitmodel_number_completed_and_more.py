# Generated by Django 4.0.5 on 2022-07-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0006_rename_task_taskmodel_remove_habitmodel_repetition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitmodel',
            name='number_completed',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='streak',
        ),
        migrations.AlterField(
            model_name='habitmodel',
            name='duration',
            field=models.CharField(choices=[('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY')], default='DAILY', max_length=255),
        ),
    ]