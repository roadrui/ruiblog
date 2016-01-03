#!/usr/bin python3
# -*- coding: utf-8 -*
from django.conf.urls import patterns,url
from django.views.generic import DetailView
from ruiblog.models import BlogsPost
__author__ = 'OnroadRui'

urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$','ruiblog.views.detail',name='detail'),
)



