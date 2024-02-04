from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.User_logout,name='logout'),
    path('register/',views.User_register,name='register'),
    
]
    