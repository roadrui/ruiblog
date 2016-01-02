from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^index/$','ruiblog.views.index'),
    url(r'^register/$','ruiblog.views.register'),
    url(r'^ruiblog/',include('ruiblog.urls',namespace="ruiblog")),
)
