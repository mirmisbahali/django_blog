from django.contrib import admin
from django.urls import path
from myblog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name="new"),

]
