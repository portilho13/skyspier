from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('insert', views.insert, name="insert")
    path("aircraft/<int:id>", views.aircraft, name="aircraft"),
    path("database/<str:value>", views.database, name="database"),
    path("flight/", views.flight, name="flight")
]