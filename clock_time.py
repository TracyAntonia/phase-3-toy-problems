# Converting time
def to_24_hour(hour, minute, period):
    # add 12 hours
    if period == "pm" and hour != 12:
        hour += 12
    # set hour to 0
    elif period == "am" and hour == 12:
        hour = 0

    # Put in in 24-hour strings
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Combine the time
    time_24_hour = hour_str + minute_str

    return time_24_hour

# Testing the codes
print(to_24_hour(8, 30, "am")) 
print(to_24_hour(12, 0, "pm"))  
