#!/usr/bin python3
# -*- coding: utf-8 -*
from django.conf.urls import patterns,url
__author__ = 'OnroadRui'

urlpatterns = patterns('',
    url(r'^index/$','ruiblog.views.index'),
    url(r'^register/$','ruiblog.views.register'),
    url(r'^login/$','ruiblog.views.login'),
)


