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
#Задача 3: Из восьмиричной в десятичную
# n = input("Введите число в восьмеричной системе счисления: ")
#
#
# def oct_to_dec(number_hex):
#     number_dec = int(number_hex, base = 8)
#     print(f"{number_hex} в десятичной {number_dec}")
#
#
# oct_to_dec(n)

#Задача 4: Дробные числа перевести в целые со степенью, где основание 1 ≤ a < 10

n = float(input("Введите число: "))


def number_with_degree(number):
    count = 0
    if number >= 10:
        while number >= 10:
            number = number / 10
            count += 1

    if number <= 1:
        while number <= 1:
            number = number * 10
            count +=1

    print(f"{number}*10^-{count}")

number_with_degree(n)