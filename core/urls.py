from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name = 'index2'),    
    url(r'^about', views.about, name = 'about'),
)