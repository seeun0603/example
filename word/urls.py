from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('upload/', views.upload, name ='upload'),
    path('upload_DB/', views.upload_DB, name ='upload_DB'),
    path('word/', views.word, name ='word'),
    path('test/', views.test, name= 'test'),
    path('check/',views.check,name ='check')
]
