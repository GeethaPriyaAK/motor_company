from django.urls import path
from . import views

urlpatterns=[
    path('home',views.car),
    path('bike',views.bike)
]