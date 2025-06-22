from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-application/', views.submit_application, name='submit_application'),
]
