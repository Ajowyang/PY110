mins_per_day = 1440

def after_midnight(time_str):
    hrs_and_min = time_str.split(':')
    hrs = int(hrs_and_min[0])
    mins = int(hrs_and_min[1])
    result = ((60 * hrs) + mins) % mins_per_day
    return result

def before_midnight(time_str):
    result = (mins_per_day - after_midnight(time_str)) % mins_per_day
    return result

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
