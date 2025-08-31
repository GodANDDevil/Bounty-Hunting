from BountyHunting import views
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='Index'),
    path('LoginScout/',views.LoginScout,name='LoginScout'),
    path('LoginSeeker/',views.LoginSeeker,name='LoginSeeker'),
    path('RegisterScout/',views.RegisterScout,name='RegisterScout'),
    path('RegisterSeeker/',views.RegisterSeeker,name='RegisterSeeker'),
    # path('LoginScout/', views.index, name='login_index'),
    path('HomepageScout/', views.HomepageScout, name='HomepageScout'),
    path('HomepageSeeker/', views.HomepaheSeeker, name='HomepageSeeker'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    path('PostJob/', views.PostJob, name='PostJob'),
    path('Apply/', views.Apply, name='Apply'),
]
