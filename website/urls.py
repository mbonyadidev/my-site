from django.urls import path
from website.views import *

urlpatterns = [
    path('', Index_view),
    path('about' , About_view),
    path ('contact', Contact_view)
]
