from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'memcachedcloud_django_sample.views.home', name='home'),
    url(r'^command$', 'memcachedcloud_django_sample.views.command', name='command'),
)

urlpatterns += staticfiles_urlpatterns()
