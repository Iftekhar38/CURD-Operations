# Generated by Django 4.2 on 2024-10-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curdApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='school',
            field=models.CharField(max_length=70),
        ),
    ]
