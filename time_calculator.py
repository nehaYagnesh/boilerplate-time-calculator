def add_time(starttime, duration, dayoftheweek=None):

    days_in_week = (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
        )
    day_index = 0
    meridian_total_list = ['AM', 'PM']
    number_of_days = 0
    time_, meridian = starttime.split()
    meridian_l = [meridian]  
    hours, minutes = (int(i) for i in time_.split(':'))
    add_hours, add_minutes = (int(d) for d in duration.split(':'))

    # Converting the starttime into hours 
    starttime_hours = round(minutes/60, 2) + hours
    
    # Converting starttime to 24 hr format
    if 'PM' in meridian:
        starttime_hours += 12
    
    # Converting the duration into hours
    duration_add_hours = (round(add_minutes/60, 2) 
                          + round(add_hours, 2))

    # Adding duration to starttime
    total_time_24format_decimal = '{:.2f}'.format(starttime_hours 
                                                  + duration_add_hours)
   
    # Converting the total time from decimal hours to hours and minutes
    totaltime_hours, totaltime_mins = (int(t) for t in total_time_24format_decimal.split('.'))
    totaltime_mins = round(totaltime_mins*60 / 100)
    if totaltime_mins < 10 :       # if minutes if not a two digit number append 0 at the start
        totaltime_mins = '0' + str(totaltime_mins)                       

    # Converting the total time in 12 hr format
    if totaltime_hours < 12:
        total_hour_12format = totaltime_hours
    elif 12 <= totaltime_hours < 24:
        total_hour_12format = totaltime_hours - 12
        if total_hour_12format == 0:
            total_hour_12format = 12
        if abs(totaltime_hours - hours) < 12:
            meridian_total_list.remove(meridian)
            meridian_l = meridian_total_list    

    if dayoftheweek is not None:
        dayoftheweek_format = dayoftheweek.lower().capitalize()
        day_index = days_in_week.index(dayoftheweek_format)
    
    while totaltime_hours >= 24:
        totaltime_hours = totaltime_hours - 24
        day_index += 1
        number_of_days += 1
        if meridian in meridian_total_list:
            if (totaltime_hours - hours == 0 
                and number_of_days == 1):
                meridian_l[0] = meridian
            elif (abs(totaltime_hours - hours) > 12 
                  or number_of_days == 1):
                meridian_total_list.remove(meridian)
                meridian_l = meridian_total_list
        if totaltime_hours == 0:
            totaltime_hours = 12
        total_hour_12format = totaltime_hours

    new_time = (str(total_hour_12format) 
                + ':' 
                + str(totaltime_mins)
                + ' '
                + str(meridian_l[0]))
    if dayoftheweek is not None:
        if number_of_days > 1:
            new_time += (', ' 
                         + days_in_week[day_index % 7] 
                         + ' (' 
                         + str(number_of_days)
                         + ' days later)')
        elif number_of_days == 1:
            new_time += (', ' 
                         + days_in_week[day_index % 7] 
                         + ' (next day)')
        else: 
            new_time += (', ' 
                         + days_in_week[day_index % 7])
    elif number_of_days == 1:
        new_time += ' (next day)'
    elif number_of_days > 1:
        new_time += (' ('
                     + str(number_of_days) 
                     + ' days later)')
    
    return new_time
