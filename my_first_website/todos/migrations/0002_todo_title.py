# Generated by Django 3.1.7 on 2021-03-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='New Title', max_length=80),
        ),
    ]
