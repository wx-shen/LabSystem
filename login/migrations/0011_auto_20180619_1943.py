# Generated by Django 2.0.4 on 2018-06-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_academicmonograph_conferencearticle_softwarepatent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencearticle',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patent',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patent',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='softwarepatent',
            name='method',
            field=models.CharField(max_length=50),
        ),
    ]
