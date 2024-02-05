from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.User_logout,name='logout'),
    path('register/',views.User_register,name='register'),
    path('record/<int:pk>',views.User_record, name='record'),
    path('delete_record/<int:pk>',views.delete_record, name='delete'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>',views.update_record, name='update_record'),

]
    