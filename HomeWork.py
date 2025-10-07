from datetime import datetime

def get_days_from_today(date_str):
    """
    Розраховує кількість днів між заданою датою і сьогоднішньою датою.

    Параметри:
    date_str (str): рядок дати у форматі 'YYYY-MM-DD'

    Повертає:
    int: кількість днів. Від'ємне число, якщо дата у майбутньому.
    """
    try:
        # Перетворюємо рядок у об'єкт datetime
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату без урахування часу
        today = datetime.today().date()
        
        # Розрахунок різниці у днях
        delta = today - target_date
        
        return delta.days
    except ValueError:
        # Викидаємо зрозумілу помилку, якщо формат дати неправильний
        raise ValueError("Неправильний формат дати. Очікується 'YYYY-MM-DD'.")

# Припустимо, сьогодні 2021-05-05
print(get_days_from_today("2021-10-09"))  # 157
print(get_days_from_today("2021-05-01"))  # 4
print(get_days_from_today("2021-05-10"))  # -5

import random

def get_numbers_ticket(min_val, max_val, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел для лотереї.

    Параметри:
    min_val (int): мінімальне число (>=1)
    max_val (int): максимальне число (<=1000)
    quantity (int): кількість чисел для вибору

    Повертає:
    list: відсортований список унікальних випадкових чисел або пустий список при некоректних параметрах
    """
    # Перевірка вхідних даних
    if not (1 <= min_val <= max_val <= 1000) or not (1 <= quantity <= (max_val - min_val + 1)):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Сортування
    numbers.sort()
    return numbers
    #
    # Вибір 6 унікальних чисел від 1 до 49
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Некоректні параметри
print(get_numbers_ticket(10, 5, 3))  # []

# Вибір 5 чисел від 1 до 36
print(get_numbers_ticket(1, 36, 5))

import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до стандартного формату для України:
    залишає тільки цифри та символ '+', додає код '+38', якщо його немає.

    Параметри:
    phone_number (str): рядок з телефонним номером у будь-якому форматі

    Повертає:
    str: нормалізований номер телефону
    """
    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    # Якщо номер починається з '+380', залишаємо як є
    if phone_number.startswith('+380'):
        return phone_number

    # Якщо номер починається з '380', додаємо '+'
    elif phone_number.startswith('380'):
        return '+' + phone_number

    # Якщо номер починається з '0', додаємо '+38'
    elif phone_number.startswith('0'):
        return '+38' + phone_number

    # Для інших випадків додаємо '+38' на початок
    else:
        return '+38' + phone_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

