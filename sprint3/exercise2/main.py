def punctuation_remove(input_string: str) -> str:
    """
    Функция принимает на вход строку, удаляет из нее знаки препинания и пробелы и возвращает результат.
    """

    result_string = input_string

    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

    for letter in input_string:
        if letter in punctuations:
            result_string = result_string.replace(letter, "")

    return result_string


def is_palindrome(input_string: str) -> bool:
    """
    Функция принимает на вход строку и выдает true если она является полиндромом, иначе false
    """

    input_string = punctuation_remove(input_string.lower())
    print(input_string)
    temp_string = input_string[::-1]

    if input_string == temp_string:
        return True

    return False


def main():
    user_str = input("Введите строку: ")

    print(is_palindrome(user_str))


if __name__ == "__main__":
    main()
