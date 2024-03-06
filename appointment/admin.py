from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'datatime', 'title', 'detail', 'user', 'status', 'created', 'updated', 'deleted']
    search_fields = ['id', 'title', 'user']
    readonly_fields = ['created', 'updated', 'deleted']
