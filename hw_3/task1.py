def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("деление на ноль невозможно")
    return x / y

def power(x, y):
    return x ** y

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Выход")

    choice = input("Введите номер операции: ")

    if choice == '6':
        print("Выход.")
        break

    if choice not in {'1', '2', '3', '4', '5'}:
        print("Неверный ввод.3")
        continue

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введены неверные данные.")
        continue

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print("Ошибка:", e)
            continue
    elif choice == '5':
        result = power(num1, num2)

    print("Результат:", result)