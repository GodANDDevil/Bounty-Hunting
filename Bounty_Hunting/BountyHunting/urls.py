from BountyHunting import views
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='Index'),
    path('LoginScout/',views.LoginScout,name='LoginScout'),
    path('LoginSeeker/',views.LoginSeeker,name='LoginSeeker'),
    path('RegisterScout/',views.RegisterScout,name='RegisterScout'),
    path('RegisterSeeker/',views.RegisterSeeker,name='RegisterSeeker'),
]
