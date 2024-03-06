from datetime import datetime


def qs_data_logic(request):
    create_dict = request.POST
    date = datetime.strptime(create_dict['date'], "%Y-%m-%d")
    hour = int(create_dict['hour'])
    minute = int(create_dict['minute'])
    ampm = create_dict['ampm']
    title = create_dict['title']
    detail = create_dict['detail']
    if ampm == 'PM' and hour != 12:
        hour += 12
    appointment_datetime = datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=hour,
        minute=minute,
    )
    return title, detail, appointment_datetime