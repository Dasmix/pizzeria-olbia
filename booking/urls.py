from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Home url
    path('', views.HomeView.as_view(), name='home'),
    # Booking url
    path('booking/', views.ReservationCreate.as_view(),
         name='book_table'),
    # List url
    path('booking/list/', views.ReservationListView.as_view(),
         name='book_manage'),
    # Detail url
    path('booking/detail/<pk>/', views.ReservationDetailView.as_view(),
         name='book_confirm'),
    # Update url
    path('<pk>/update', views.ReservationUpdateView.as_view(),
         name='book_edit'),
    # Delete url
    path('<pk>/delete/', views.ReservationDeleteView.as_view(),
         name='book_delete'),
]
