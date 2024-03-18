from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signUp/', views.signUp_user, name='signUp'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
]