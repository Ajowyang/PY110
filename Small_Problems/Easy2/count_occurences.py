def count_occurrences(lst):
    counter = {}    
    for element in lst:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    for (key, val) in counter.items():
        print(f"{key} = > {val}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
