while True:
    num_elements = int(input("Введите количество элементов в списке: "))
    elements = []

    for i in range(num_elements):
        element = input(f"Введите элемент {i + 1}: ")
        elements.append(element)

    exponent = int(input("Введите степень: "))

    for element in elements:
        try:
            element = float(element)
            result = element ** exponent
        except ValueError:
            result = element * exponent
        print(f"{element} в степени {exponent} равно {result}")
