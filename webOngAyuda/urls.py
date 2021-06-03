
from django.contrib import admin
from django.urls import path
from .views import index, Cachulo, Flaca, gato, Ginger, Lucifer, Niña, Perro, Tommy

urlpatterns = [
    path('', index, name='IND'),
    path('Cachulo/', Cachulo, name='CAC'),
    path('Flaca/', Flaca, name='FLACA'),
    path('Gato/', gato, name='GATO'),
    path('Ginger/', Ginger, name='GINGER'),
    path('Lucifer/', Lucifer, name='LUCI'),
    path('Niña/', Niña, name='NIÑA'),
    path('Perro/', Perro, name='PERRO'),
    path('Tommy/', Tommy, name='TOMMY'),

]
