from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),

    path('order', views.create_order, name='create_order'),
    path('view_orders', views.view_orders, name='view_orders'),
    # path('insert', views.insertData, name='insertData'),
    path('update/<id>', views.updateData, name='updateData'),
    path('delete/<id>', views.delete, name='deleteData'),

]
