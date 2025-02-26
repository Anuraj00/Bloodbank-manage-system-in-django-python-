from django.contrib import admin
from django.urls import path

from Guest import views

app_name="Guest"

urlpatterns = [
    path('DonorRegistration/',views.donorInsert,name="donorInsert"),
    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
]
