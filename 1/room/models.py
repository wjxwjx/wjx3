from django.db import models
from django.contrib import admin
xname = []
class User(models.Model):
    name = models.CharField(max_length=30)
    SID = models.IntegerField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __unicode__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=30)
    building = models.ForeignKey(Building)

    def __unicode__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=30)
    seating_num = 100
    appointment = models.IntegerField(max_length=3)
    appointment.default = 0
    floor = models.ForeignKey(Floor)
    building = models.ForeignKey(Building)
    week = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    people = models.ManyToManyField(User,related_name = "people")
    people.blank = True
    flag = models.BooleanField()
    flag.default = False
    def __unicode__(self):
        return self.name


admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Classroom)
admin.site.register(User)


