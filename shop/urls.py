from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexfunction,name="admindashbord"),
    path("registration", views.registration, name="registration"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),
    path("userhome", views.userhome, name="userhome"),
    path("contact", views.contactform, name="contact"),
    path('home', views.home, name='home'),
    # path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('buyproducts', views.buyproducts, name='buyproducts'),
    path('admindashbord', views.admindashbord, name='admindashbord'),
    path('service', views.service, name='service'),

    ]