import datetime as datetime1
from datetime import datetime, date, time
import calendar
from app1.models import *


def get_progress_table(user,user_class):

    lessons1=Lessons.objects.all()
    lessons = OneLesson.objects.all()
    mygrade = Grade.objects.filter(student=user)
    grade = Grade.objects.all()


    #----------------------------------------------
    #первый семестр
    d1 = date(datetime.now().year, 9, 1)
    d2 = date(datetime.now().year, 10, 27)

    #второй семестр

    d3 = date(datetime.now().year, 8, 11)
    d4 = date(datetime.now().year, 12, 22)

    #третий семестр

    d5 = date(datetime.now().year, 1, 11)
    d6 = date(datetime.now().year, 3, 27)

    #четвёртый семестр

    d7 = date(datetime.now().year, 4, 5)
    d8 = date(datetime.now().year, 5, 31)

    # первый семестр
    d11=date(datetime.now().year, 9, 1)
    d12=date(datetime.now().year, 12, 31)

    # второй семестр
    d13=date(datetime.now().year, 1, 1)
    d14=date(datetime.now().year, 6, 1)

    #-------------------------------



    a=[]

    for lesson in  lessons:
        list=[]

        #1 добавляем в лист урок
        list.append(lesson)

        #2 добавляем в лист моё за месяц
        #date(datetime.now().year,datetime.now().month, 1)<=grade_date<=date(datetime.now().year,datetime.now().month, calendar.monthrange(datetime.now().year, datetime.now().month)[1])
        mygrade2=mygrade.filter(grade_date__gte=date(datetime.now().year,datetime.now().month, 1)).filter(grade_date__lte=date(datetime.now().year,datetime.now().month, calendar.monthrange(datetime.now().year, datetime.now().month)[1])).filter(lesson=lesson).filter(student=user)
        t=0
        z=0
        #2
        for mygr in mygrade2:
            t=t+mygr.grade
            z=z+1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")

        #3 добавляем в лист всех за месяц
        grade3=grade.filter(grade_date__gte=date(datetime.now().year, datetime.now().month, 1)).filter(grade_date__lte=date(datetime.now().year, datetime.now().month,calendar.monthrange(datetime.now().year, datetime.now().month)[1])).filter(lesson=lesson).filter(student=user)
        t = 0
        z = 0
        # 2
        for gr in grade3:
            t = t + gr.grade
            z = z + 1
        if(z!=0):
            list.append(round(t / z, 1))
        if(z==0):
            list.append("-")



        #4 добавляем в лист себя за 1 четверть
        if datetime.now().month>=9:
            mygrade4=mygrade.filter(grade_date__gte=d1).filter(grade_date__lte=d2).filter(lesson=lesson).filter(student=user)
        if datetime.now().month <= 9:
            mygrade4=mygrade.filter(grade_date__gte=d5).filter(grade_date__lte=d6).filter(lesson=lesson).filter(student=user)
        t = 0
        z = 0
        # 2
        for mygr in mygrade4:
            t = t + mygr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")

        # 5 добавляем в лист всех за 1 четверть
        if datetime.now().month >= 9:
            grade5=grade.filter(grade_date__gte=d1).filter(grade_date__lte=d2).filter(lesson=lesson).filter(student=user)
        if  datetime.now().month <=9:
            grade5=grade.filter(grade_date__gte=d5).filter(grade_date__lte=d6).filter(lesson=lesson).filter(student=user)


        t = 0
        z = 0
        # 2
        for gr in grade5:
            t = t + gr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")

        # 6 добавляем в лист себя за 2 четверть
        if datetime.now().month >= 9:
            mygrade6=mygrade.filter(grade_date__gte=d3).filter(grade_date__lte=d4).filter(lesson=lesson).filter(student=user)
        if datetime.now().month <= 9:
            mygrade6=mygrade.filter(grade_date__gte=d7).filter(grade_date__lte=d8).filter(lesson=lesson).filter(student=user)

        t = 0
        z = 0
        # 2
        for mygr in mygrade6:
            t = t + mygr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")

        # 7 добавляем в лист всех за 2 четверть
        if datetime.now().month >= 9:
            grade7=grade.filter(grade_date__gte=d3).filter(grade_date__lte=d4).filter(lesson=lesson).filter(student=user)
        if datetime.now().month <= 9:
            grade7=grade.filter(grade_date__gte=d7).filter(grade_date__lte=d8).filter(lesson=lesson).filter(student=user)

        t = 0
        z = 0
        # 2
        for gr in grade7:
            t = t + gr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")

        # 8 добавляем в лист всех за семестр
        if datetime.now().month >= 9:
            mygrade8=mygrade.filter(grade_date__gte=d11).filter(grade_date__lte=d12).filter(lesson=lesson).filter(student=user)
        if datetime.now().month <= 9:
            mygrade8=mygrade.filter(grade_date__gte=d13).filter(grade_date__lte=d14).filter(lesson=lesson).filter(student=user)

        t = 0
        z = 0
        # 2
        for mygr in mygrade8:
            t = t + mygr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")


        #9 добавляем в лист себя за  семестр

        if datetime.now().month >= 9:
            grade9=grade.filter(grade_date__gte=d11).filter(grade_date__lte=d12).filter(lesson=lesson).filter(student=user)
        if datetime.now().month <= 9:
            grade9=grade.filter(grade_date__gte=d13).filter(grade_date__lte=d14).filter(lesson=lesson).filter(student=user)

        t = 0
        z = 0
        # 2
        for gr in grade9:
            t = t + gr.grade
            z = z + 1
        if (z != 0):
            list.append(round(t / z, 1))
        if (z == 0):
            list.append("-")


        a.append(list)





    return a



def get_timetable(date, user_class):
    time_list = OneLesson.objects.filter(date=date).filter(a_class=user_class)
    lessons_and_time = [{'number': 1, 'time': '09:00-09:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 2, 'time': '10:00-10:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 3, 'time': '11:00-11:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 4, 'time': '12:00-12:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 5, 'time': '13:00-13:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 6, 'time': '14:00-14:45', 'title': 'нет урока', 'homework': '', 'comment': ''},
                        {'number': 7, 'time': '15:00-15:45', 'title': 'нет урока', 'homework': '', 'comment': ''}
                        ]
    for lesson in time_list:
        one_lesson = list(filter(lambda x: x['time'] == str(lesson.lesson_time), lessons_and_time))[0]
        if str(lesson != ''):
            one_lesson['title'] = str(lesson)
        one_lesson['homework'] = lesson.homework
        one_lesson['comment'] = lesson.comment_teacher
    return lessons_and_time


def get_timetable_week(date, user_class):
    date_from = date - datetime1.timedelta(days=date.weekday())
    date_to = date + datetime1.timedelta(days=6 - date.weekday())
    result = []
    while date_from <= date_to:
        result.append({'date': get_date_to_string(date_from), 'lessons': get_timetable(date_from, user_class)})
        date_from += datetime1.timedelta(days=1)
    return result


def get_date_to_string(date):
    week_days = ['понедельник', 'вторник', 'среду', 'четверг', 'пятница', 'субботу', 'воскресенье']
    return week_days[date.weekday()] + ' ' + date.strftime('%d.%m.%Y')

