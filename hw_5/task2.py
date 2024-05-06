import calendar
import re

def check_number(number):
    regex = r"^(?:\+7|7|8)\d{10}$"
    return re.match(regex, number)

def generate_calendar(date_str):
    if not re.match(r"\d{4}-\d{2}", date_str):
        return "Неверный формат даты."

    year, month = map(int, date_str.split('-'))
    cal = calendar.month(year, month)
    return cal

date_input = input("Введите дату в формате ГГГГ-ММ: ")
if generate_calendar(date_input):
    print(generate_calendar(date_input))
else:
    print("Некорректная дата.")

phone_number = input("Введите номер телефона: ")
if check_number(phone_number):
    print("Корректный номер телефона.")
else:
    print("Некорректный номер телефона.")
