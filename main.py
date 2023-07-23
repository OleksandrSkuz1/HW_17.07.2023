
    # ЗАВДАННЯ 1

    # Напишіть функцію, яка відобразить на екрані такий форматований текст:
    # "Don't compare yourself with anyone in this world…if you do so, you are insulting yourself."
# def my_function():
#         text = "Don't compare yourself with anyone in this world…if you do so, you are insulting yourself"
#         print(text)
# my_function()


    # ЗАВДАННЯ 2
    # Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

# def my_numbers(numOne, numTwo):             # створюємо функцію з двома параметрами
#
#     for num in range(numOne, numTwo + 1):   # створюємо цикл
#         if num % 2 == 0:                    # cтворюємо умову для парного числа
#          print(num)
# my_numbers(1, 20)                           # виклик функції з заданими параметрами


    # ЗАВДАННЯ 3

    # Напишіть функцію, яка відображає порожній або заповнений квадрат з певного символу.
    # Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:
        #якщо вона дорівнює True, квадрат заповнений;
        #якщо — False, квадрат порожній.

# def draw_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         for row in range(side_length):
#             if row == 0 or row == side_length - 1:
#                 print(symbol * side_length)
#             else:
#                 print(symbol + " " * (side_length - 2) + symbol)
#
# # Приклад виклику функції з параметрами
# draw_square(5, "*", True)
# print()
# draw_square(5, "#", False)


    # ЗАВДАННЯ 4

    # Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри.

# def my_numbers(a, b, c, d, e):
#     return min(a, b, c, d, e)
#
# minNumber = my_numbers(35, 7, 99, 14, 22)
# print("Мінімальне число: ", minNumber)


    # ЗАВДАННЯ 5

    # Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
    # Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.

# def product_in_range(start, end):
#     # Перевірка, чи початкове число менше за кінцеве
#     if start > end:
#         start, end = end, start
#
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
#
#     return product
#
# # Приклад виклику функції з числами 5 та 25 (переплутані межі)
# result = product_in_range(5, 25)
# print("Добуток чисел у діапазоні:", result)


    # ЗАВДАННЯ 6
    # Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр.
    # З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.

# def my_fuction(number):
#     return len(str(abs(number)))
#
# number = 5524647
#
# result = my_fuction(number)
# print("Кількість цифр у числі: ", result)


    # ЗАВДАННЯ 7
    # Напишіть функцію, яка перевіряє, чи є число паліндромом. Число передається як параметр.
    # Якщо число є паліндромом, потрібно повернути з функції true, якщо ні — false.
    # Паліндром — це число, у якого перша частина цифр рівноцінна другій дзеркально відображеній частині цифр.
    # Наприклад, 123321 — паліндром (перша частина – 123, друга частина – 321, повернувши яку отримаємо 123).
    # 546645 — паліндром, а 421987 — не паліндром.