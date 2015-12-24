from django.conf.urls import patterns, include, url
from django.contrib import admin
from room.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classroom.views.home', name='home'),
    # url(r'^classroom/', include('classroom.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$',Login),
    (r'^home/$',Home),
    (r'^sign/$',Sign),
    (r'^logout/$',logout),
    (r'^show/$',information),
    (r'^showp/$',showP),
    (r'^showdetails1/$',show1),
    (r'^showdetails2/$',show2),
    (r'^showdetails3/$',show3),
    (r'^showdetails4/$',show4),
    url(r'^admin/', include(admin.site.urls)),
)
