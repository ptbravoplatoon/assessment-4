from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page')
]