'''
Created on 20 janv. 2016

@author: jerome
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
