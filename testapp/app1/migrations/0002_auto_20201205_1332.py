# Generated by Django 3.1.2 on 2020-12-05 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='onelesson',
            unique_together={('date', 'lesson_time', 'a_class')},
        ),
    ]