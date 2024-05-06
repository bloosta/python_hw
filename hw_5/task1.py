import random

def random_elements(list):
    return random.choices(list, k=2)

list = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
print(random_elements(list))

