def swap_name(name):
    names = name.split(" ")
    result = f"{names[len(names)-1]}, {' '.join(names[0:len(names) - 1])}"
    return result

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
