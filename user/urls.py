from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('second/third/', views.third, name='third-nested'),
    path('second/third/fourth/', views.fourth, name='fourth-nested'),
    path('second/third/fourth/fifth/',views.fifth,name='fifth-nested'),
    path('second/third/fourth/fifth/seventh/',views.seventh,name='seventh-nested'),
    path('second/third/fourth/fifth/seventh/eighth/', views.eighth, name='eighth-nested'),
    path('second/third/fourth/fifth/index',views.index,name='index-nested'),

]