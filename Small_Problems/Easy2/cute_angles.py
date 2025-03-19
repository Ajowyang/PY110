DEGREE = "\u00B0"

def dms(angle_degrees):
    num_degrees = angle_degrees // 1
    
    angle_degrees_decimal = angle_degrees % 1
    num_minutes = angle_degrees_decimal // (1 / 60) 
    
    remaining_degrees = angle_degrees_decimal - ( num_minutes * (1 / 60) )
    num_seconds = remaining_degrees // (1 / 3600) 
    result = f"{num_degrees:0,.0f}{DEGREE}{num_minutes:02.0f}'{num_seconds:02.0f}\""
    print(result)
    return result



# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
