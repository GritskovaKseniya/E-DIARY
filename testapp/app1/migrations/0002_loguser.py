# Generated by Django 3.1.2 on 2020-12-04 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.students')),
            ],
        ),
    ]