def total_ages(dict):
    result = 0
    for age in dict.values():
        result += age
    return result

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
print(total_ages(ages))
