from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('signup/', views.signup, name='singup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]