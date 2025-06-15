from django.urls import path
from .views import ListingListCreateView, BookingListCreateView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
]
