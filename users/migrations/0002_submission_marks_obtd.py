# Generated by Django 3.2.7 on 2021-11-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='marks_obtd',
            field=models.IntegerField(default=0),
        ),
    ]
