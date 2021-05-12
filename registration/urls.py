from django.urls import path
from registration import views
urlpatterns = [
    path('upload/', views.simple_upload),
    path('', views.history, name='history'),
    path('apply/', views.application, name='apply')
]