from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('presidentLogin/', signin),
    path('presidentIndex/', index),
    path('presidentDoctorView/', president_doctor_view),
    path('presidentPatientView/', president_patient_view),
    path('presidentPatientAdd/',president_patient_addition),
    path('presidentDoctorAdd/',president_doctor_addition)
]