from django.urls import path
from curdApp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('addnew/', views.addNew, name='addnew'),
    path('display/', views.display, name='display'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('updaterecord/<id>', views.updateRecord, name='updaterecord'),
    path('deleterecord/<id>', views.deleteRecord, name='deletereocrd')

]