# Generated by Django 2.2.3 on 2019-11-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantmodel',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
