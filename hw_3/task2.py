def mult_list(listmlp : list, mult: float | int = 2) -> list:
    new_list= []
    for x in listmlp:
        x *= mult
        new_list.append(x)
    return new_list

print("Список:\n[1,2,3]")
print("Функция:")
print(mult_list([1,2,3], 2))

mult_lambda = lambda list_to_mlp, mult = 2: [x * mult for x in list_to_mlp]

print("Лямбда функция:")
print(mult_lambda([1, 2, 3], 2))

