from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.shop, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signUp/', views.signUp_user, name='signUp'),
]