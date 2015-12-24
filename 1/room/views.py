from django.shortcuts import *
from models import User,Floor,Classroom,Building
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import models

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def Login(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name',''):
            errors.append('请填写用户名。')
        if not request.POST.get('password',''):
            errors.append('请填写密码。')
        try:
            user = User.objects.get(name = request.POST['name'])
            username = user.name
            if user is not None and user.password == request.POST['password']:
                request.session['user_id'] = user.name
                return render_to_response('homepage.html',locals())
            else:
                errors.append("密码不正确！")      
        except User.DoesNotExist:
            errors.append("用户不存在！")
    return render_to_response('login.html',locals())

def Home(request):
    try:
        username = request.session['user_id']
        if request.session['user_id']: 
            return render_to_response('homepage.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')

def Sign(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name',''):
            errors.append('请填写用户名。')
        if not request.POST.get('sid',''):
            errors.append('请填写学号。')
        if not request.POST.get('email',''):
            errors.append('请填写邮箱。')
        if not request.POST.get('password',''):
            errors.append('请填写密码。')
        temp =  User.objects.filter(name=request.POST['name'])
        if temp:
            errors.append("用户已经存在！")
        if not errors:
            post = request.POST
            user = User(name=post['name'],
                        SID=post['sid'],
                        email=post['email'],
                        password=post['password'],)
            user.save()
            return HttpResponsePermanentRedirect('/')
    return render_to_response('sign_up.html',locals())

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def information(request):
    try:
        username = request.session['user_id']
        if request.session['user_id']:   
            user = User.objects.get(name = request.session['user_id'])
            return render_to_response("information.html",locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')

def showP(request):
    try:
        username = request.session['user_id']
        if request.session['user_id']:   
            user = User.objects.get(name = request.session['user_id'])
            if 'floor' in request.GET:
                temp = Classroom.objects.filter(floor__name = request.GET['floor'],
                                                     name = request.GET['name'],
                                                     week = request.GET['week'],
                                                     number = request.GET['number'],)
                temp[0].people.remove(user)
                num = temp[0].appointment
                num -= 1
                temp.update(appointment = num,
                            flag = False)
                
            classrooms = user.people.all()
            return render_to_response('showp.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')
def show1(request): 
    try:
        if request.session['user_id']:   
            Bname = u'正心'
            username = request.session['user_id']
            errors = []
            classrooms = []
            if 'number' and 'week' in request.GET:
                number  = request.GET['number']
                week = request.GET['week']
                if not number or not week:
                    error = True
                else:
                    floors = Floor.objects.filter(building__name__icontains=Bname)
                    user = User.objects.get(name = request.session['user_id'])
                    temp = user.people.all()
                    for x in floors:
                        classroom = Classroom.objects.filter(floor = x,
                                                             number = number,
                                                             week = week,)
                        classroom.update(flag = False)
                        for y in classroom:
                            if y in temp:
                                y.flag = True
                                y.save()
                        classrooms.append(classroom)
            if 'name1' in request.GET:
                name1 = request.GET['name1']
                week1 = request.GET['week1']
                number1 = request.GET['number1']
                classroom = Classroom.objects.filter(name=name1,
                                                 week = week1,
                                                 number = number1,)
                num = classroom[0].appointment
                num += 1
                user = User.objects.get(name = request.session['user_id'])
                if classroom[0].flag:
                    errors.append("您已经预约过该教室！")
                elif num > 100:
                    errors.append("该教室预约人数已满！")
                else:
                    classroom[0].people.add(user)
                    classroom.update(appointment = num,flag = True)
                floors = Floor.objects.filter(building__name__icontains=Bname)
                for x in floors:
                    classroom = Classroom.objects.filter(floor = x,
                                                            number = number1,
                                                            week = week1,)
                    classrooms.append(classroom)
            return render_to_response('show_details.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')

def show2(request):
    try:
        if request.session['user_id']:  
            username = request.session['user_id']
            Bname = u'管理'
            errors = []
            classrooms = []
            if 'number' and 'week' in request.GET:
                number  = request.GET['number']
                week = request.GET['week']
                if not number or not week:
                    error = True
                else:
                    floors = Floor.objects.filter(building__name__icontains=Bname)
                    user = User.objects.get(name = request.session['user_id'])
                    temp = user.people.all()
                    for x in floors:
                        classroom = Classroom.objects.filter(floor = x,
                                                             number = number,
                                                             week = week,)
                        classroom.update(flag = False)
                        for y in classroom:
                            if y in temp:
                                y.flag = True
                                y.save()
                        classrooms.append(classroom)
            if 'name1' in request.GET:
                name1 = request.GET['name1']
                week1 = request.GET['week1']
                number1 = request.GET['number1']
                classroom = Classroom.objects.filter(name=name1,
                                                 week = week1,
                                                 number = number1,)
                num = classroom[0].appointment
                num += 1
                user = User.objects.get(name = request.session['user_id'])
                if classroom[0].flag:
                    errors.append("您已经预约过该教室！")
                elif num > 100:
                    errors.append("该教室预约人数已满！")
                else:
                    classroom[0].people.add(user)
                    classroom.update(appointment = num,flag = True)
                floors = Floor.objects.filter(building__name__icontains=Bname)
                for x in floors:
                    classroom = Classroom.objects.filter(floor = x,
                                                            number = number1,
                                                            week = week1,)
                    classrooms.append(classroom)
            return render_to_response('show_details.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')

def show3(request):
    try:
        if request.session['user_id']:   
            username = request.session['user_id']
            Bname = u'格物'
            errors = []
            classrooms = []
            if 'number' and 'week' in request.GET:
                number  = request.GET['number']
                week = request.GET['week']
                if not number or not week:
                    error = True
                else:
                    floors = Floor.objects.filter(building__name__icontains=Bname)
                    user = User.objects.get(name = request.session['user_id'])
                    temp = user.people.all()
                    for x in floors:
                        classroom = Classroom.objects.filter(floor = x,
                                                             number = number,
                                                             week = week,)
                        classroom.update(flag = False)
                        for y in classroom:
                            if y in temp:
                                y.flag = True
                                y.save()
                        classrooms.append(classroom)
            if 'name1' in request.GET:
                name1 = request.GET['name1']
                week1 = request.GET['week1']
                number1 = request.GET['number1']
                classroom = Classroom.objects.filter(name=name1,
                                                 week = week1,
                                                 number = number1,)
                num = classroom[0].appointment
                num += 1
                user = User.objects.get(name = request.session['user_id'])
                if classroom[0].flag:
                    errors.append("您已经预约过该教室！")
                elif num > 100:
                    errors.append("该教室预约人数已满！")
                else:
                    classroom[0].people.add(user)
                    classroom.update(appointment = num,flag = True)
                floors = Floor.objects.filter(building__name__icontains=Bname)
                for x in floors:
                    classroom = Classroom.objects.filter(floor = x,
                                                            number = number1,
                                                            week = week1,)
                    classrooms.append(classroom)
            return render_to_response('show_details.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')

def show4(request):
    try:
        if request.session['user_id']:   
            Bname = u'致知'
            username = request.session['user_id']
            errors = []
            classrooms = []
            if 'number' and 'week' in request.GET:
                number  = request.GET['number']
                week = request.GET['week']
                if not number or not week:
                    error = True
                else:
                    floors = Floor.objects.filter(building__name__icontains=Bname)
                    user = User.objects.get(name = request.session['user_id'])
                    temp = user.people.all()
                    for x in floors:
                        classroom = Classroom.objects.filter(floor = x,
                                                             number = number,
                                                             week = week,)
                        classroom.update(flag = False)
                        for y in classroom:
                            if y in temp:
                                y.flag = True
                                y.save()
                        classrooms.append(classroom)
            if 'name1' in request.GET:
                name1 = request.GET['name1']
                week1 = request.GET['week1']
                number1 = request.GET['number1']
                classroom = Classroom.objects.filter(name=name1,
                                                 week = week1,
                                                 number = number1,)
                num = classroom[0].appointment
                num += 1
                user = User.objects.get(name = request.session['user_id'])
                if classroom[0].flag:
                    errors.append("您已经预约过该教室！")
                elif num > 100:
                    errors.append("该教室预约人数已满！")
                else:
                    classroom[0].people.add(user)
                    classroom.update(appointment = num,flag = True)
                floors = Floor.objects.filter(building__name__icontains=Bname)
                for x in floors:
                    classroom = Classroom.objects.filter(floor = x,
                                                            number = number1,
                                                            week = week1,)
                    classrooms.append(classroom)
            return render_to_response('show_details.html',locals())
    except KeyError:
       pass
    return HttpResponsePermanentRedirect('/')