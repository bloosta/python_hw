dict = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dict.keys())
values_set = set(dict.values())
combined_set = keys_set | values_set

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединенное множество:", combined_set)