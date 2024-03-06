from django.urls import path
from .views import (
    get_appointments, create_appointment, edit_appointment, delete_appointment, accept_appointment, reject_appointment
)

urlpatterns = [
    path('get/', get_appointments, name="appointments"),
    path('create/', create_appointment, name="appointment_create"),
    path('edit/<int:id>/', edit_appointment, name="appointment_edit"),
    path('delete/<int:id>/', delete_appointment, name="appointment_delete"),
    path('accept/<int:id>/', accept_appointment, name="appointment_accept"),
    path('reject/<int:id>/', reject_appointment, name="appointment_reject"),
]
