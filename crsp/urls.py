from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('register', views.register_user, name='register'),
    path('profile', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]
