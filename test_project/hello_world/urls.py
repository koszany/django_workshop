from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hello_world-home'),
    path('about/', views.about, name='hello_world-about'),
    path('search/', views.request_page, name='hello_world-search')
]
