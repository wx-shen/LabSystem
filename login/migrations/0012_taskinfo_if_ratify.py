# Generated by Django 2.0.4 on 2018-06-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20180619_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinfo',
            name='if_ratify',
            field=models.IntegerField(default=0),
        ),
    ]