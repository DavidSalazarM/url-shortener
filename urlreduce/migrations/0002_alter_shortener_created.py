# Generated by Django 3.2.9 on 2021-11-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlreduce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]