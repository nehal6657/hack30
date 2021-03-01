from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', views.index, name="home"),
<<<<<<< HEAD
    path('shedule', views.output, name='shedule'),
    
    
]
=======
    path('shedule',views.output, name='shedule'),
    path('register', views.register, name='register'),
    path('login', views.index, name='login'),
]
>>>>>>> eac7e668bda762ef93b5c2e650983a5f05b99547
