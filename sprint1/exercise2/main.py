def sleight_of_hand(k: int, field: str) -> int:
    """
    Функция нахождения максимального количество баллов которые могут получить два игрока\n
    На вход принимает колличетво кнопок которые они могу нажать (k) и матрицу кнопок (field)\n
    На выходе отдается максимальное количество быллов которые они смогли набрать\n
    """
    result = 0
    field = list(field)

    for courent_button in range(1, 10):
        courent_button_count = field.count(str(courent_button))
        if (courent_button_count > 0) and (k >= courent_button_count):
            result += 1

    print(f"Максимальное количество баллов: {result}")
    return result


def main():
    print("Введите число: ")
    button_count = int(input())
    button_count *= 2

    print("Введите матрицу: ")
    mas = ""
    for _ in range(4):
        mas += input()

    sleight_of_hand(button_count, mas)


if __name__ == "__main__":
    main()
