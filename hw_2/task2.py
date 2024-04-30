while True:
    user_input = input("Введите слово:\n")
    user_input = user_input.lower()

    dictionary = {}

    for letter in user_input:
        if letter != ' ':
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1

    print(f"{dictionary}")
