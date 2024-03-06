from django.shortcuts import render, redirect
from .models import Appointment
from .utils import qs_data_logic
from django.db.models import Q

def get_appointments(request):
    if request.user.is_staff:
        lookups = Q(deleted=False) # & (Q(status=True) | Q(status=None))
        qs = Appointment.objects.filter(lookups).order_by('datatime')
    else:
        qs = Appointment.objects.filter(user=request.user, deleted=False).order_by('datatime')
    context = {
        "appointments": qs
    }
    return render(request, 'appointment/appointments.html', context)


def create_appointment(request):
    if request.method == "POST":
        title, detail, appointment_datetime = qs_data_logic(request)
        lookups = Q(deleted=False) & Q(datatime=appointment_datetime) & Q(status=True)
        qs =  Appointment.objects.filter(lookups)
        if qs.exists():
            context = {
                "error": "for this data time appointment is booked so please select other data or time"
            }
            return render(request, 'appointment/create_appointment.html', context)
        Appointment.objects.create(
            title=title,
            detail=detail,
            datatime=appointment_datetime,
            user=request.user
        )
        return redirect('appointments')
    context = {}
    return render(request, 'appointment/create_appointment.html', context)


def edit_appointment(request, id=None):
    qs = Appointment.objects.get(id=id)
    if request.method == "POST":
        print("update")
        title, detail, appointment_datetime = qs_data_logic(request)
        lookups = Q(deleted=False) & Q(datatime=appointment_datetime) & Q(status=True)
        qs = Appointment.objects.filter(lookups)
        if qs.exists():
            context = {
                "error": "for this data time appointment is booked so please select other data or time"
            }
            return render(request, 'appointment/create_appointment.html', context)
        qs = Appointment.objects.get(pk=id)
        qs.title = title
        qs.detail = detail
        qs.datatime = appointment_datetime
        qs.save()
        return redirect('appointments')
    hour = qs.datatime.hour - 12
    minute = qs.datatime.minute
    context = {
        'appointment': qs,
        'hour': str(hour),
        'minute': str(minute),
    }
    return render(request, 'appointment/edit_appointment.html', context)


def delete_appointment(request, id=None):
    context = {}
    qs = Appointment.objects.get(id=id)
    qs.deleted = True
    qs.save()
    return redirect('appointments')


def accept_appointment(request, id=None):
    context = {}
    qs = Appointment.objects.get(id=id)
    qs.status = True
    qs.save()
    return redirect('appointments')


def reject_appointment(request, id=None):
    context = {}
    qs = Appointment.objects.get(id=id)
    qs.status = False
    qs.save()
    return redirect('appointments')
