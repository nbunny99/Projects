from django.urls import path
from .views import availability, booking, home, data, delete_data, book_form

urlpatterns = [
    path('', home, name='home'),
    path('availability/', availability, name='preview'),
    path('booking/', booking, name='book'),
    path('data/', data, name='data'),
    path('delete/<int:id>/', delete_data, name='delete'),
    path('bookform', book_form, name='form'),
]
