# Generated by Django 4.2.3 on 2023-07-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0002_userloginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginmodel',
            name='password',
            field=models.CharField(max_length=100, verbose_name='pass'),
        ),
    ]
