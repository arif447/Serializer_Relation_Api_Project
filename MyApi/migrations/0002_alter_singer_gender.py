# Generated by Django 4.1.1 on 2022-10-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
