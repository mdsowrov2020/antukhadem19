from django.urls import path,include
from maison_home import views
urlpatterns = [
    path('',views.Home,name='home'),
]