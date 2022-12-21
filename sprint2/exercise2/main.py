def largest_number(n: int, numbers: list) -> str:
    output_number = ""
    for _ in range(n):
        max_number = "0"
        for number in numbers:
            max_number_len = len(max_number)
            number_len = len(number)
            if number_len > max_number_len:
                temp_number = number[0:max_number_len]
                if temp_number > max_number:
                    max_number = number
                elif temp_number == max_number:
                    if number[-1] > max_number[0]:
                        max_number = number

            elif number_len < max_number_len:
                temp_number = max_number[0:number_len]

                if temp_number < number:
                    max_number = number
                elif temp_number == number:
                    if max_number[-1] < number[0]:
                        max_number = number

            if number_len == max_number_len:
                if number > max_number:
                    max_number = number
        numbers.remove(max_number)
        output_number += max_number
    return output_number


def main():
    numbers = []

    print("Введите количество чисел: ")
    numbers_count = int(input())

    print("Введите числа: ")
    for _ in range(numbers_count):
        numbers.append(input())

    print(largest_number(numbers_count, numbers))


if __name__ == "__main__":
    main()
