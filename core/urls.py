'''
Created on Sep 23, 2017

@author: dayo_bf
'''
from django.conf.urls import url, include


from .views import *

urlpatterns = [
    url(r'^user/$', Uapp.as_view(), name='uapp'),
    url(r'^africastalking_callback/$', ACUSSDCallback.as_view(), name='acussd'),
]