def add_time(starttime, duration, dayoftheweek=None):
    new_time = ''
    days_in_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day_index = 0
    total_hour_12format = 0
    meridian_total_list = ['AM','PM']
    number_of_days = 0
    time,meridian = starttime.split()
    meridian_l = [meridian]  
    hours,minutes = time.split(':')
    add_hours,add_minutes = duration.split(':')

    # Converting the starttime into hours
    startminutes_hours =  ''.join('{:.2f}').format(int(minutes) / 60)
    starttime_hours = float(startminutes_hours) + int(hours)
    
    # Converting starttime to 24 hr format
    if 'PM' in meridian : starttime_hours += 12
    
    # Converting the duration into hours
    duration_minutes_hours  = ''.join('{:.2f}').format(int(add_minutes) / 60)
    duration_add_hours = float(''.join('{:.2f}').format(float(duration_minutes_hours)))+ float(''.join('{:.2f}').format(float(add_hours)))

    # Adding duration to starttime
    total_time_24format_decimal = starttime_hours + duration_add_hours
    total_time_24format_decimal = ''.join('{:.2f}').format(total_time_24format_decimal)
   
    # Converting the total time from decimal hours to hours and minutes
    totaltime_hours,totaltime_minutes = str(total_time_24format_decimal).split('.')
    totaltime_minutes = round((int(totaltime_minutes) * 60) / 100)
    if totaltime_minutes < 10 :       # if minutes if not a two digit number append 0 at the start
        totaltime_minutes = '0' + str(totaltime_minutes)                       

    # Converting the total time in 12 hr format
    if int(totaltime_hours) < 12 :
        total_hour_12format = totaltime_hours
    elif int(totaltime_hours) >= 12 and int(totaltime_hours) < 24:  # if the totaltimehours is greater than 12 but less than 24
        total_hour_12format = int(totaltime_hours) - 12
        if total_hour_12format == 0:
            total_hour_12format = 12
        if abs(int(totaltime_hours) - int(hours)) < 12:
            meridian_total_list.remove(meridian)
            meridian_l = meridian_total_list    
    if dayoftheweek is not None:
        dayoftheweek_format = dayoftheweek.lower().capitalize()   # returns a string with the first letter of the string as capital whereas other letter as small 
        day_index = days_in_week.index(dayoftheweek_format)
    
    while int(totaltime_hours) >= 24:     # If the totaltimehours is greater then 24 then subtract by 24
        totaltime_hours = int(totaltime_hours) - 24
        day_index += 1
        number_of_days += 1
        if meridian in meridian_total_list and (totaltime_hours - int(hours) == 0 and number_of_days ==1):
            meridian_l[0] = meridian
        elif meridian in meridian_total_list and (abs(totaltime_hours - int(hours)) > 12 or number_of_days ==1 ):
            meridian_total_list.remove(meridian)
            meridian_l = meridian_total_list
        if totaltime_hours == 0:
            totaltime_hours = 12
        total_hour_12format = totaltime_hours
    if dayoftheweek is not None:
        if number_of_days > 1:
            new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0]) + ', ' + days_in_week[day_index % 7] + ' (' + str(number_of_days) + ' days later)'
        elif number_of_days == 1:
            new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0]) + ', ' + (days_in_week[day_index % 7]) + ' (next day)'
        else: 
            new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0]) + ', ' + days_in_week[day_index % 7]
    elif dayoftheweek is None and number_of_days == 1:
        new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0]) + ' (next day)'
    elif dayoftheweek is None and number_of_days > 1:
        new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0]) + ' (' + str(number_of_days) + ' days later)'
    else:
        new_time = str(total_hour_12format) + ':' + str(totaltime_minutes)+ ' '+ str(meridian_l[0])
    return new_time
