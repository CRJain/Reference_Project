# Generated by Django 2.2 on 2020-05-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200524_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
