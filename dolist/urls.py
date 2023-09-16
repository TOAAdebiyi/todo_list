from django.urls import path
from . import views # . dot means from the same directory that this file is

urlpatterns = [
    # load page of the app that will be sending the index.html file
    path('',views.index, name='index')
]
