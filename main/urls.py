from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('signup', views.signup, name='signup'),
    path('post/create/', views.createpost, name='createpost'),
    path('post/list/', views.listpost, name='listpost'),
    path('post/view/<int:pk>', views.viewpost, name='viewpost'),
    path('post/edit/<int:pk>', views.editpost, name='editpost'),
    path('post/delete/<int:pk>', views.deletepost, name='deletepost'),
    path('reset/', views.PasswordReset, name='password_reset'),

]