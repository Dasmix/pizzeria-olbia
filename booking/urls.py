from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('book_table/', views.book_table, name='book_table'),
    path('manage_reservation/', views.manage_reservation, name='manage_reservation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
