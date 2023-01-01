number_dec = int(input("Введите число: "))

def dec_to_bin(number_dec):
    first = bin(number_dec)
    number_bin = first[2:]
    print(f"{number_dec} в двоичной системе {number_bin}")

    second = oct(number_dec)
    number_oct = second[2:]
    print(f"{number_dec} в восьмиричной системе {number_oct}")

    third = hex(number_dec)
    number_hex = third[2:]
    print(f"{number_dec} в восьмиричной системе {number_hex}")


dec_to_bin(number_dec)

