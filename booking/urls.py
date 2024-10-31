from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('book_table/', views.book_table, name='book_table'),
    path('manage_reservation/', views.manage_reservation, name='manage_reservation'),
]
