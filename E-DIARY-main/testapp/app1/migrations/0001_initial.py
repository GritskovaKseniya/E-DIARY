# Generated by Django 3.1.2 on 2020-12-07 21:08

import datetime
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
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('is_active', models.BooleanField(default=True, verbose_name='Работает/Учится')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_begin', models.TimeField(unique=True)),
                ('time_end', models.TimeField(unique=True)),
            ],
            options={
                'verbose_name': 'Время урока',
                'verbose_name_plural': 'Время уроков',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('is_active', models.BooleanField(default=True, verbose_name='Работает/Учится')),
                ('user_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.classes')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='OneLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('homework', models.CharField(blank=True, max_length=500)),
                ('lesson_status', models.IntegerField(choices=[(1, 'Активный'), (2, 'Отменен'), (3, 'Замена')], default=1)),
                ('a_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.classes')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.lessons')),
                ('lesson_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.timeslot')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.teachers')),
            ],
            options={
                'verbose_name': 'Расписание урока',
                'verbose_name_plural': 'Расписание уроков',
            },
        ),
        migrations.CreateModel(
            name='LogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.students')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('grade_type', models.IntegerField(choices=[(1, 'Работа на уроке'), (2, 'Самостоятельная работа'), (3, 'Контрольная работа'), (4, 'Домашняя работа')])),
                ('grade_date', models.DateField(default=datetime.date.today)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.onelesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.students')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.AddConstraint(
            model_name='onelesson',
            constraint=models.UniqueConstraint(fields=('date', 'lesson_time', 'a_class'), name='unique_lesson'),
        ),
    ]
