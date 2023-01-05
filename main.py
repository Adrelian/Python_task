# Задача 1: Из десятичной в двоичную
# number_dec = int(input("Введите число: "))
#
#
# def dec_to_bin(number_dec):
#     first = bin(number_dec)
#     number_bin = first[2:]
#     print(f"{number_dec} в двоичной системе {number_bin}")
#
#     second = oct(number_dec)
#     number_oct = second[2:]
#     print(f"{number_dec} в восьмиричной системе {number_oct}")
#
#     third = hex(number_dec)
#     number_hex = third[2:]
#     print(f"{number_dec} в восьмиричной системе {number_hex}")
#
#
# dec_to_bin(number_dec)
# Задача 1: Из разных систем в десятичную
# n = input("Введите число: ")
#
#
# def hex_to_dec(number):
#     number_dec = int(number, base=16)
#     print(f"{number} в десятичной {number_dec}")
#
#
# def oct_to_dec(number):
#     number_dec = int(number, base=8)
#     print(f"{number} в десятичной {number_dec}")
#
#
# def bin_to_dec(number):
#     number_dec = int(number, base=2)
#     print(f"{number} в десятичной {number_dec}")
#
#
# bin_to_dec(n)
#
# Задача 3: Из восьмиричной в десятичную
# n = input("Введите число в восьмеричной системе счисления: ")
#
#
# def oct_to_dec(number_hex):
#     number_dec = int(number_hex, base = 8)
#     print(f"{number_hex} в десятичной {number_dec}")
#
#
# oct_to_dec(n)
#
# Задача 4: Дробные числа перевести в целые со степенью, где основание 1 ≤ a < 10
#
# n = float(input("Введите число: "))
#
#
# def number_with_degree(number):
#     count = 0
#     if number >= 10:
#         while number >= 10:
#             number = number / 10
#             count += 1
#
#     if number <= 1:
#         while number <= 1:
#             number = number * 10
#             count +=1
#
#     print(f"{number}*10^-{count}")
#
# number_with_degree(n)
#
# Задача 6: Найти наименьшую дробь числа
#
# n = float(input("Введите десятичную дробь: "))
#
#
# def find_simple_fraction(dec_float_number):
#     denominator = 1  # знаменатель.
#     fractional_part = dec_float_number % 1  # десятичная дробная часть
#     save_number = dec_float_number
#     # Представляем дробь в виде dec_float_number / 1
#     while fractional_part != 0:
#         dec_float_number = dec_float_number * 10  # сдвигаем запятую на один вправо
#         fractional_part = dec_float_number % 1  # снова ищем числа после запятой
#         denominator *= 10
#
#     numeral = int(dec_float_number)  # числитель в int
#
#     # максимальный делитель для числителя
#     for n in range(numeral - 1, 1, -1):
#         if numeral % n == 0:
#             max_number1 = n
#             break
#
#     # максимальный делитель для знаменателя
#     for n in range(denominator - 1, 1, -1):
#         if denominator % n == 0:
#             max_number2 = n
#             break
#
#     print(f"Десятичная дробь {save_number} в простую {numeral}/{denominator}")
#
#     print(f"Наибольший делитель {numeral} равен {max_number1}")
#     print(f"Наибольший делитель {denominator} равен {max_number2}")
#
#     print(f"Простая дробь для числа {save_number} равно {int(numeral / max_number1)}/{int(denominator / max_number2)}")
#
#
# find_simple_fraction(n)
#
# Задача 7. Дано комплексное число. Выведите на экран его действительную и мнимую части, а также число, сопряженное к данному
#
# complex_number = complex(input("Введите комплексное число: "))
#
# def com_num(complex_number):
#     real = complex_number.real
#     comp = complex_number.imag
#     comj = complex_number.conjugate()
#
#     print(f"Действительная часть числа {complex_number} равна {real}")
#     print(f"Мнимая часть числа {complex_number} равна {comp}")
#     print(f"Сопряженное число с {complex_number} равно {comj}")
#
# com_num(complex_number)
#
# Задача 8. Даны два действительных числа a и b. Вычислите их сумму, разность,
# произведение и частное. Округлите результаты до сотых и выведите их на экран
#
# num_1 = float(input("Введите десятичную дробь "))
# num_2 = float(input("Введите десятичную дробь "))
#
#
# def find_result(num1, num2):
#     print(f"Cумма числе {num1} и {num2} равна {round(num1 + num2, 2)}")
#     print(f"Произведение числе {num1} и {num2} равна {round(num1 * num2, 2)}")
#     print(f"Частное числе {num1} и {num2} равна {round(num1 / num2, 2)}")
#
#
# find_result(num_1, num_2)
#
# Задача 9. Вычислите значение выражения (10/2.3 - 34)*0.7 + 90.5,
# округлив результат до трех знаков после десятичной точки и найдя его модуль
#
# num = round((10 / 2.3 - 34) * 0.7 + 90.5, 2)
# print(num)
#
#
# задача 10. Найдите значение выражения в десятичной системе счисления: (1EA16 + 010111012 - 2378 - 68110)*21023.
# num_1 = "1EA"
# num_2 = "01011101"
# num_3 = "237"
# num_4 = 681
# num_5 = "2102"
#
# num_1 = int(num_1, 16)
# num_2 = int(num_2, 2)
# num_3 = int(num_3, 8)
# num_5 = int(num_5, 3)
#
# a = (num_1 + num_2 - num_3 - num_4) * num_5
# print(a)
#
# Задача 11. Выведите на экран результат вычисления sin(π/6) и cos(45°) округлив результат до двух знаков после десятичной точки
#
# import math
# n_gradus = int(input("Введите градус угла: "))
#
#
# def gradus_cos(gradus):
#     print(f"Косинус угла в {gradus} равен {round(math.cos(gradus), 2)}")
#
#
# def radian():
#     print(f"Синус угла pi/2 равен {math.sin(math.pi/2)}")
#
#
# gradus_cos(n_gradus)
# radian()
#
# Задача 12 Вычислите значение арифметического выражения при заданных значениях переменных
# и выведите полученный результат на экран: 5.2a3 + 3b5 - 7.3 при a=3, b=2.5.
#
# def find_result():
#     a = 3
#     b = 2.5
#     c = round(5.2 * pow(a, 3) + 3 * pow(b, 5) - 7.3, 2)
#     print(c)
#
#
# find_result()
#
# Задача 13. Вычислите значение арифметического выражения при заданных значениях переменных
# и выведите полученный результат на экран: x(3.3 + 2y) - |64:(x + y)| при x=-4.1, y=2.
#
# def find_result():
#     x = - 4.1
#     y = 2
#     z = x * (3.3 + 2 * y) - abs(64 / (x + y))
#     print(round(z, 2))
#
# find_result()
#
# Задача 14. Вычислите значение арифметического выражения при заданных значениях переменных
# и выведите полученный результат на экран: |m(2m-1) - 35.5|:(3n + 0.8m)2 при m=2, n=5.
#
# def find_result():
#     m = 2
#     n = 5
#     o = abs(pow(m, 2 * m - 1) - 35.5) / (3 * n + 0.8 * m) * 2
#     print(round(o, 2))
#
#
# find_result()
#
# Задача 14. Вычислите значение арифметического выражения при заданных значениях переменных
# и выведите полученный результат на экран: log4(7x - 3y) + √(lg|10xy|) при x=4, y=-3.
#
# from math import sqrt
# from math import log2, log10
# def find_result():
#     x = 4
#     y = -3
#     z = log2(7 * x - 3 * y) + sqrt(log10(abs(10 * x * y)))
#     print(round(z, 2))
#
#
# find_result()
#
# Задача 15: Вычислите значение арифметического выражения при заданных значениях переменных
# и выведите полученный результат на экран: √(log2(mn+2 - 3e)):(ln(2m) + lg(4n)) при m=5, n=2.
#
# def find_result():
#     m = 5
#     n = 2
#     o = math.sqrt(math.log2(m * n + 2 - 3 * math.e)) / (math.log(2 * m) + math.log(4 * n))
#     print(round(o, 2))
#
# find_result()
#
# Задача 16. Запишите арифметическое выражение на языке Python,
# а затем выведите полученный результат на экран: cos2(3a - 1) - sin(5a - b)3.
#
#
# def find_result():
#     a = int(input('Введите a: '))
#     b = int(input('Введите b: '))
#     c = (1 + math.cos(2 * (3 * a - 1))) - math.sin(5 * a - b) * 3
#     print(round(c, 2))
#
# find_result()
#
# Задача 17. Запишите арифметическое выражение на языке Python,
# а затем выведите полученный результат на экран: 3tg|√(x + y2) - π| - arctg3(√x + y2).
#
# def find_result():
#     x = int(input('Введите х: '))
#     y = int(input('Введите y: '))
#     z = 3 * math.tan(abs(math.sqrt(x + y * 2) - math.pi)) - math.atan(3 * (math.sqrt(x) + y * 2))
#     print(round(z, 2))
#
#
# find_result()
#
# Задача 18. Запишите арифметическое выражение на языке Python,
# а затем выведите полученный результат на экран: √(arccos3x - arcsin2y)/arctg|x2 - y2| + 5√π
#
# from cmath import *
# def find_result():
#     x = 1 / 3
#     y = 1 / 3
#     z = (sqrt(math.acos(3 * x) - math.asin(2 * y))) /(math.atan(abs(x * 2 - y * 2)) + 5 * sqrt(math.pi))
#     print(z)
#
#
# find_result()
#
# Задача 19. Запишите арифметическое выражение на языке Python,
# а затем выведите полученный результат на экран: √(arccos3x - arcsin2y)/arctg|x2 - y2| + 5√π
#
# from cmath import sqrt
# def find_result():
#     x = 1/3
#     y = 1/2
#     z = (sqrt(math.acos(3 * x) - math.asin(2 * y)))/ (math.atan(abs(x * 2 - y * 2) + 5 * math.sqrt(math.pi)))
#     print(z)
#
#
# find_result()
#
# Задача 20. Вычислите значение арифметического выражения |3√π4 - 8eπ|/ln9.7.
# Округлите результат до сотых и выведите его на экран.
#
# def find_result():
#     z = (abs(pow(math.sqrt(math.pi * 4), 1/3) - 8 * math.e * math.pi)) / math.log(9.7)
#     print(round(z, 3))
#
# find_result()
#
# Задачи по строкам
#
# def user_input():
#     number_int = int(input("Введите целое число: "))
#     number_float = float(input("Введите дробное десятичное число: "))
#     number_complex = complex(input("Введите комплексное число: "))
#
#     print(f"Числа в формате string: {number_int}, {number_float}, {number_complex}")
#     print(f'Числа в формате string: {number_int}, {number_float}, {number_complex}')
#
# user_input()
#
# Задача 22. Составьте и выведите на экран пользователя строку-матрешку
# с содержимым «'4 + "3 + '2 + "1 + '0' " ' " '».
# Реализуйте вывод четырьмя способами, использовав в качестве внешних все виды кавычек, разрешенных для строк.
#
# def matreshka():
#     n = int(input("Введите число: "))
#     end = 0
#     while n > end:
#         print(f'"{n}" + ', end="")
#         n = n - 1
#
# matreshka()
#
# Задача 23. Дана строка '123456789'. Используя операции индексирования
# и среза выведите на экран третий и пятый символы, а также подстроку '567'.
# Реализуйте вывод двумя способами: используя только положительные индексы и только отрицательные.
#
# def str_index():
#     num = str(123456789)
#     print(f"Третий символ строки {num[2]}, подсчет сначала строки")
#     print(f"Пятый символ строки {num[4]}, подсчет сначала строки")
#     print(f"Срез строки {num[4:7]}")
#
#     print(f"Третий символ строки {num[-7]}, подсчет с конца строки")
#     print(f"Пятый символ строки {num[-5]}, подсчет с конца строки")
#
#
# str_index()
#
# Задача 24. Дана строка 'AaBbCcDd'. Используя срезы с шагом получите две строки:
# только с заглавными и только со строчными буквами. Выведите их на экран.
#
# def slices():
#     first_string = str('AaBbCcDd')
#     second_string = first_string[0:len(first_string):2]
#     print(second_string)
#     third_string = first_string[1:len(first_string):2]
#     print(third_string)
#
#
# slices()
