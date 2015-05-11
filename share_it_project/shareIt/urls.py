from django.conf.urls import patterns, url
from shareIt import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^images$', views.images, name='images'),
        url(r'^images/upload$', views.uploadImage, name="uploadImage"),
        url(r'^about', views.about, name="about")
        )