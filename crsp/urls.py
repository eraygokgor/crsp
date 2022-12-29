from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('register', views.register_user, name='register'),
    path('signin', views.signin, name='signin'),
    path('settings', views.settings, name='settings'),
    path('logout', views.logout, name='logout'),
    path('changes', views.changes, name='changes'),
    path('delete', views.delete, name='delete'),
]
