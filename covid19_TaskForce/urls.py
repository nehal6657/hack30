from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('index', views.index, name="home"),
    path('shedule',views.output, name='shedule'),
    path('register', views.register, name='register'),
    path('login', views.index, name='login'),
=======
    
    path('index', views.index, name="home"),
    path('shedule',views.output, name='shedule')
>>>>>>> acac3dd672b98318acc5d189d1bb5c9a23621547
]