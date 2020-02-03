from django.urls import path
from .views import *

app_name = 'shreebalaji'

urlpatterns = [
    path('', index, name='index'),
    path('galleries/', galleries, name='gallaries'),
    path('services', Services.as_view(), name='services'),
    path('aboutus', AboutUs.as_view(), name='aboutus'),
    path('contactus', ContactUs.as_view(), name='contactus'),
    path('ongoing', Ongoing.as_view(), name='ongoing'),
    path('completed', Completed.as_view(), name='completed'),
]
