
# from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home),
    url(r'^page$', views.somepage),
    url(r'^count/', views.countwords, name='count'),
    url(r'^about/', views.about, name='about')
    # url(r'', views.error404),
]
