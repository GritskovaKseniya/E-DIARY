# Generated by Django 3.1.2 on 2020-11-02 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('user_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.classes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OneLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('homework', models.CharField(blank=True, max_length=500)),
                ('lesson_type', models.IntegerField(choices=[(1, 'Active'), (2, 'Canceled'), (3, 'Switched')])),
                ('a_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.classes')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.lessons')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('grade_type', models.IntegerField(choices=[(1, 'Lesson Work'), (2, 'Test'), (3, 'Control Test')])),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.onelesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.student')),
            ],
        ),
    ]