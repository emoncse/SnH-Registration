from django.urls import path
from registration import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.application, name='application'),
]