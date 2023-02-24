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
#
# Задача 2.6 Измените строку 'кот', записав ее символы в обратном порядке. Выведите результат на экран.
#
# def reverse_str():
#     a = "cat"
#     b = a[::-1]
#     print(b)
#
#
# reverse_str()
#
# Задача 2.7. Дана строка '0123456789'. Удалите из нее первый, пятый и последний символы. Выведите результат на экран
#
#
# def delete_symbol():
#     a = "0123456789"
#     b = a[1:5:1] + a[6:9:1]
#     print(b)
#
# delete_symbol()
#
# Задача 2.8 При помощи строк '.', '!' и ' ' (один пробел) сформируйте новую строку '..... ! ! ! .....' и выведите ее на экран.
# Разрешается использовать только операторы + и *.
#
#
# def  new_str():
#     a = "."
#     b = "!"
#     c = " "
#     new = a * 5 + c + b * 3 + c + a * 5
#     print(new)
#
#
# new_str()
#
# Задача 2.9 'Дана строка 'Вот и пришла осень золотая!'.
# Возьмите ее в кавычки «» и выведите результат на экран. Шестнадцатиричные коды кавычек в Юникоде: 00AB и 00BB.
#
# print("\u0022Вот и пришла осень золотая!\u0022")

# 2.10.* Подсчитайте количество символов в строке '1a\u0398\t\u03B43s'.
# Сделайте это сперва устно, а затем проверьте себя программно.

# def array_search(A:list, N:int, x:int):
#     """
#     Осуществляет поиск числа X в массиве А.
#     От 0 до N-1 индекса включительно
#     Если в массиве несколько элементов равных Х, то вернуть индекс первого по счёту
#     :param A:
#     :param N:
#     :param x:
#     :return: индекс элемента х в массиве А или -1, если такого числа нет
#     """
#     for k in range(N):
#         if A[k] == x:
#             return k
#     return -1
#
#
# def test_array_search():
#     A1 = [1, 2, 3, 4, 5]
#     m = array_search(A1, 5, 8)
#     if m == -1:
#         print("#test1 - ok")
#     else:
#         print("test1 - fail")
#
#     A2 = [-1, -2, -3, -4, -5]
#     m = array_search(A2, 5, -3)
#     if m == 2:
#         print("#test2 - ok")
#     else:
#         print("test2 - fail")
#
#     A3 = [10, 20, 30, 10, 10]
#     m = array_search(A3, 5, 10)
#     if m == 0:
#         print("#test3 - ok")
#     else:
#         print("test3 - fail")
#
# test_array_search()


# def invert_array(arr:list, size_arr:int):
#     """
#     Разворот массива
#     в рамках индекса от 0 до -1
#     :param arr: входной массив
#     :param size_arr: размер массива
#     :return:
#     """
#     for k in range(size_arr//2):
#         arr[k], arr[size_arr - 1 - k] = arr[size_arr - 1 - k], arr[k]
#
#
# def test_invert_array():
#     a1 = [1, 2, 3, 4, 5]
#     print(a1)
#     invert_array(a1, 5)
#     print(a1)
#     if a1 == [5, 4, 3, 2, 1]:
#         print("#test1 - ok")
#     else:
#         print("test1 - fail")
#
#     a2 = [0, 0, 0, 0, 0, 0, 0, 0, 10]
#     print(a2)
#     invert_array(a2, 9)
#     print(a2)
#     if a2 == [10, 0, 0, 0, 0, 0, 0, 0, 0]:
#         print("#test2 - ok")
#     else:
#         print("test2 - fail")
#
# test_invert_array()

# arr = [1, 2, 3, 4, 5,]
# temp = arr[0]
# for k in range(len(arr) - 1):
#     arr[k] = arr[k + 1]
# arr[len(arr) - 1] = temp
#
# print(arr)

# arr = [True] * 100
# print(arr)
# arr[0] = arr[1] = False
# for k in range(2, 100):
#     if arr[k]:
#         for m in range(k*k, 100, k):
#             arr[m] = False
# print(arr)
# for k in range(100):
#     print(k, "-", "простое" if arr[k] else "составное")


# def matryoshka (n):
#     if n == 1:
#         print("Матрёшечка")
#     else:
#         print("Верх мартешка, n=", n)
#         matryoshka(n-1)
#         print("Низ матрёшки n=", n)
#
# matryoshka(5)
#
# import graphics as gr
# window = gr.GraphWin("Game", 600, 600)
# alpha = 0.8
#
#
# def fractal(A, B, C, D, deep=100):
#     if deep < 1:
#         return
#     for M, N in [(A, B), (B, C), (C, D), (D, A)]:
#         gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
#     A1 = (A[0] * (1 - alpha) + B[0] * alpha,
#           A[1] * (1 - alpha) + B[1] * alpha)
#     B1 = (B[0] * (1 - alpha) + C[0] * alpha,
#           B[1] * (1 - alpha) + C[1] * alpha)
#     C1 = (C[0] * (1 - alpha) + D[0] * alpha,
#           C[1] * (1 - alpha) + D[1] * alpha)
#     D1 = (D[0] * (1 - alpha) + A[0] * alpha,
#           D[1] * (1 - alpha) + A[1] * alpha)
#     fractal(A1, B1, C1, D1, deep - 1)
#
# fractal((100, 100), (500, 100), (500, 500), (100, 500))


# def factorial(n: int):
#     assert n >= 0, "Факториал отрицательного числа не определён"
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(3))

# def gcd(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return gcd(a - b, b)
#     else:  # a < b
#         return gcd(a, b - a)
#
#
# print(gcd(10, 25))
#
#
# def new_gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return new_gcd(b, a % b)
#
#
# print(new_gcd(10, 25))
#
#
# def little_gcd(a, b):
#     return a if b == 0 else little_gcd(b, a % b)
#
#
# print(little_gcd(10, 25))

# import time
# start_time = time.time()
#
#
# def power(a: float, n: int):
#     assert n > 0, "Степень должна быть положительной"
#     if n == 0:
#         return 1
#     elif n % 2 == 1:  # нечётная степень
#         return pow(a, n - 1) * a
#     else:  # степень чётная
#         return pow(a ** 2, n//2)
#
#
# (power(4, 10000000))
# print("--- %s seconds ---" % (time.time() - start_time))
#
# (power(4, 10000001))
# print("--- %s seconds ---" % (time.time() - start_time))

# import turtle
# import os
#
# turtle.shape('turtle')

# forward = 10
# x = -10
# y = -10
# for i in range(12):
#     turtle.color("green")
#     for i in range(4):
#         turtle.fd(forward)
#         turtle.lt(90)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#
#     x -= 10
#     y -= 10
#     forward = forward + 20
# n = 30
# for i in range(12):
#     turtle.fd(50)
#     turtle.stamp()
#     turtle.lt(180)
#     turtle.fd(50)
#     turtle.home()
#     turtle.lt(n)
#     n+=30
#
#
# os.system("pause")

# def genarate_number(N: int, M: int, prefix=None):
#     """
#     Функция генерирует все числа (с лидирующими нулями) в N-ричной системе счисления (N <= 10) длинны М
#     :param N: Основание системы счисления
#     :param M: длинна числа
#     :param prefix:
#     :return:
#     """
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for digit in range(N):
#         prefix.append(digit)
#         genarate_number(N, M-1, prefix)
#         prefix.pop()
#
#
# genarate_number(3, 3)


# #Однопроходный алгроритм
# def find(number, A):
#     """
#     Ищет х в А и возвращает True, если такое число есть, False если такого числа нет
#     :param number: искомое повторяющееся число
#     :param A: Список с числами
#     :return: Флаг, истина или лож в зависимости от результата
#     """
#     flag = False
#     for x in A:
#         if number == x:
#             flag = True
#             break
#     return flag
#
# def generate_permutations(N: int, M: int = -1, prefix=None):
#     """
#     Генерация всех перестановок N чисел в M позициях, начиная с префиксом prefix
#     :param N: числа от 1 до N для перебора комбинация
#     :param M: кол-во позиция для перестановки
#     :param prefix:
#     :return:
#     """
#     M = N if M == -1 else M  # по умолчанию N чисел в N позициях
#     prefix = prefix or []
#     if M == 0:
#         print(*prefix, end=", ", sep="")  # развернуть список как отдельные числа
#         return
#     for number in range(1, N + 1):
#         if find(number, prefix):
#             continue
#         prefix.append(number)
#         generate_permutations(N, M - 1, prefix)
#         prefix.pop()
#
#
# generate_permutations(5, 5)

