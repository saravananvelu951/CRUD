from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('add',views.add,name="add"),
    path('edite',views.edite,name="edite"),
    path('update/<str:id>',views.update,name="update"),
    path('delete/<str:id>',views.delete,name="delete"),
]
    