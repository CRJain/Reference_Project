# Generated by Django 2.2 on 2020-05-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200524_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
