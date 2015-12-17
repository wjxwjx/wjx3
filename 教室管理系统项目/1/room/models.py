from django.db import models
from django.contrib import admin

class User(models.Model):
    name = models.CharField(max_length=30)
    SID = models.IntegerField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=30)
    seating_num = 100
    appointment = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.ForeignKey(Classroom)

    def __unicode__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=30)
    floor = models.ForeignKey(Floor)

    def __unicode__(self):
        return self.name

admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(Floor)
admin.site.register(Building)