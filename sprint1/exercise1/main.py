def find_zero_lr(array: list, item_position: int, left: bool) -> [str, None]:
    """
    Функция поиска растояния от заданного элемента до ближайшего элемента равного нулю\n
    Если параметр left = True тогда функция ищет растояние до ближайшего элемента слева, иначе ищет справа\n
    На вход принимает массив (array) и номер элемента от которого нужно найти расстояние (item_position)\n
    На выходе возвращает расстояние до заданного элемента либо возвращает None если 0 не найден.
    """
    distance = 0

    if array[item_position] == 0:
        return str(distance)

    if left:
        for i in range(item_position, -1, -1):
            if array[i] == '0':
                return str(distance)
            distance += 1
    else:
        for i in range(item_position, len(array)):
            if array[i] == '0':
                return str(distance)
            distance += 1

    return None


def nearest_zero(array_lenght: int, array: str) -> str:
    """
    Функция поиска расстояние элемента массива до ближашего элемента массива со значением 0\n
    На вход принимает длинну массива (array_lenght) и массив (array) вида: "0 1 4 9 0"\n
    Возвращает массив вида "0 1 2 1 0"
    """

    result_array = []
    array = array.split(" ")

    # for house in array:
    for house_number in range(array_lenght):
        left_distance = find_zero_lr(array, house_number, True)
        right_distance = find_zero_lr(array, house_number, False)

        if left_distance is None:
            result_array.append(right_distance)
        elif right_distance is None:
            result_array.append(left_distance)
        elif left_distance < right_distance:
            result_array.append(left_distance)
        else:
            result_array.append(right_distance)

    result_array = " ".join(result_array)
    print(result_array)

    return result_array


def main():
    print("Введите строку домов: ")
    array = input()

    array_lenght = len(array.split(" "))
    result = nearest_zero(array_lenght, array)


if __name__ == "__main__":
    main()
