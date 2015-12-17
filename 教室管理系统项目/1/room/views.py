import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import *
from room.models import User,Floor,Classroom
from django.db import models

def Login(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name',''):
            errors.append('请填写用户名。')
        if not request.POST.get('password',''):
            errors.append('请填写密码。')
        #验证机制
        if not errors:
            return render_to_response('homepage.html',locals())
    return render_to_response('login.html',locals())

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
            return render_to_response('edit_success.html',locals())
    return render_to_response('sign_up.html',locals())

def show1(request):
    if 'id' in request.GET:
        name  = request.GET['id']
        if not name:
            error = True
        else:
            classroom = Classroom.objects.filter(name=name)
            num = classroom[0].appointment
            num += 1
            classroom.update(appointment=num)
    classrooms = []
    floors = Floor.objects.filter(name__icontains="xf")
    for floor in floors:
        classrooms.append(floor.classroom)
    Bname = u'正心'
    return render_to_response('show_details.html',locals())

def show2(request):
    if 'id' in request.GET:
        name  = request.GET['id']
        if not name:
            error = True
        else:
            classroom = Classroom.objects.filter(name=name)
            num = classroom[0].appointment
            num += 1
            classroom.update(appointment=num)
    classrooms = []
    floors = Floor.objects.filter(name__icontains="cf")
    for floor in floors:
        classrooms.append(floor.classroom)
    Bname = u'诚意'
    return render_to_response('show_details.html',locals())

def show3(request):
    if 'id' in request.GET:
        name  = request.GET['id']
        if not name:
            error = True
        else:
            classroom = Classroom.objects.filter(name=name)
            num = classroom[0].appointment
            num += 1
            classroom.update(appointment=num)
    classrooms = []
    floors = Floor.objects.filter(name__icontains="gf")
    for floor in floors:
        classrooms.append(floor.classroom)
    Bname = u'格物'
    return render_to_response('show_details.html',locals())

def show4(request):
    if 'id' in request.GET:
        name  = request.GET['id']
        if not name:
            error = True
        else:
            classroom = Classroom.objects.filter(name=name)
            num = classroom[0].appointment
            num += 1
            classroom.update(appointment=num)
    classrooms = []
    floors = Floor.objects.filter(name__icontains="zf")
    for floor in floors:
        classrooms.append(floor.classroom)
    Bname = u'致知'
    return render_to_response('show_details.html',locals())

    