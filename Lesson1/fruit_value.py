def select_fruit(dict):
    result = {}
    for key in dict:
        if dict[key] == "Fruit":
            result[key] = dict[key]
    return result

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
