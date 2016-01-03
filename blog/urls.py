#! /usr/bin python3
# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ruiblog.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$','ruiblog.views.index'),
    
   # url(r'^index/$','ruiblog.views.index'),
    url(r'^ruiblog/',include('ruiblog.urls',namespace="ruiblog")),

    url(r'^about_me/$','ruiblog.views.about_me',name="about_me"),
    
    url(r'^searchBlog/$','ruiblog.views.blog_search',name="blog_search"),
)


