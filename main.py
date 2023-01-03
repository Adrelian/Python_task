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

