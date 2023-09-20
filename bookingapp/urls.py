
from django.urls import path
from bookingapp.views import *

urlpatterns = [
   
    path('index/', indexview),
    # path('', indexview),
    path('room/', roomsview),
    path('dinning/', dinningview),
    path('gallery/', galleryview),
    path('contact/', contactview),
    path('menu/', menuview),

    path('book/', bookview),
    path('display/', displayview),
    path('update/<int:id>/', updateview),
    path('delete/<int:id>/', deleteview),
    
]