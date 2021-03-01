from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('shedule', views.output, name='shedule'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('student',views.student,name='student')
    
]
