from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('menu/<int:pk>/delete', views.DeleteSingleMenuItemView.as_view(), name='delete_menu_item'),
    path('api-token-auth/', obtain_auth_token),
    # Comment all the below to test API endpoints above.
    path('booking/', views.booking, name='booking'),
    path('booking/<int:pk>/', views.bookingDetail, name='booking_detail'),
    path('booking/add/', views.addBooking, name='add_booking'),
    path('booking/<int:pk>/update/', views.updateBooking, name='update_booking'),
    path('booking/<int:pk>/delete/', views.deleteBooking, name='delete_booking'),
]