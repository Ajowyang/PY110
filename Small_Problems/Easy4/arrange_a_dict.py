def order_by_value(dict):
    dict_items = [(t[1], t[0]) for t in list(dict.items())]
    dict_items.sort()
    return [t[1] for t in dict_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
