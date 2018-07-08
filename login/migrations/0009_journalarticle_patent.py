# Generated by Django 2.0.4 on 2018-06-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_property_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author_id', models.IntegerField()),
                ('journal_name', models.CharField(max_length=50)),
                ('publish_time', models.CharField(max_length=20)),
                ('roll_num', models.IntegerField()),
                ('start_end_page', models.CharField(max_length=20)),
                ('task_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('patent_num', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('category', models.IntegerField()),
                ('status', models.IntegerField()),
                ('apply_for_time', models.CharField(max_length=50)),
                ('take_effect_time', models.CharField(max_length=50)),
                ('task_id', models.IntegerField()),
                ('author_id', models.IntegerField()),
            ],
        ),
    ]
