# Generated by Django 3.1.2 on 2020-12-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201205_1332'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='onelesson',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='onelesson',
            constraint=models.UniqueConstraint(fields=('date', 'lesson_time', 'a_class'), name='unique_lesson'),
        ),
    ]