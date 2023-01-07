def convert_dec_to_bin(number: int) -> str:
    """
    Функция принимает на вход число в десятичной системе счесления и отдает число в двоичной системе.
    """

    output = ""
    while number // 2 != 0:
        output += str(number % 2)
        number = number // 2
    output += str(number % 2)

    return output[::-1]


def main():
    number = int(input("Введите число: "))

    print(convert_dec_to_bin(number))


if __name__ == "__main__":
    main()
