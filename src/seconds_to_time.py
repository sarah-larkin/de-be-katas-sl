def seconds_to_time(num): 
    hours = num // 3600
    minutes = (num - (hours * 3600)) // 60
    seconds = num - (hours * 3600) - (minutes * 60)

    hour_stamp = 'hour' if hours == 1 else 'hours'
    minute_stamp = 'minute' if minutes == 1 else 'minutes'
    second_stamp = 'second' if seconds == 1 else 'seconds'

    #hours, mins, secs
    if hours and minutes and seconds: 
        return f'{hours} {hour_stamp}, {minutes} {minute_stamp} and {seconds} {second_stamp}'
    #hours only
    if hours and not minutes and not seconds: 
        return f'{hours} {hour_stamp}'
    #mins, secs
    if not hours and minutes and seconds: 
        return f'{minutes} {minute_stamp} and {seconds} {second_stamp}'
    #mins only
    if not hours and minutes and not seconds: 
        return f'{minutes} {minute_stamp}'
    #secs only
    if not hours and not minutes and seconds: 
        return f'{seconds} {second_stamp}'
   


