def add_time(min):
    time_hrs = 0
    time_mins = 0

    hrs_to_add = min // 60
    mins_to_add = min % 60
   
    time_hrs = time_hrs + hrs_to_add
    time_mins = time_mins + mins_to_add
    
    if time_hrs >= 24:
        time_hrs = time_hrs % 24
        
    result = f"{time_hrs:02d}:{time_mins:02d}"
    print(result)
    return result


def subtract_time(min):
    time_hrs = 23
    time_mins = 60
    
    hrs_to_subtract = (-min) // 60
    mins_to_subtract = (-min) % 60
    
    time_hrs = time_hrs - hrs_to_subtract
    time_mins = time_mins - mins_to_subtract
    print(time_hrs)
    if time_hrs < 0:
        time_hrs = 24 - (-(time_hrs) % 24)
    
    result = f"{time_hrs:02d}:{time_mins:02d}"
    print(result)
    return result

def time_of_day(min):
    if min == 0:
        print("00:00")
        return "00:00"
    elif min > 0:
        return(add_time(min))
    else:
        return(subtract_time(min))	




print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
print(time_of_day(-5671) == "01:29")    # True
