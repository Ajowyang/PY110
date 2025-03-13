def select_fruit(dict):
    result = {}
    for curr_key, curr_value in dict.items():
        if curr_value == "Fruit":
            result[curr_key] = curr_value
    return result

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
