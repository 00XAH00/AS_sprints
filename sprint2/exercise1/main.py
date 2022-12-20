brackets_sequences = []


def psp(n: int, bracket_open: int, bracket_close: int, sequence: str = "") -> None:
    if (bracket_close + bracket_open) == (2 * n):
        brackets_sequences.append(sequence)
    else:
        if bracket_open < n:
            # sequence += "("
            psp(n, bracket_open+1, bracket_close, sequence+"(")
        if bracket_open > bracket_close:
            # sequence += ")"
            psp(n, bracket_open, bracket_close+1, sequence+")")


def main():
    print("Введите число: ")
    number = int(input())

    psp(number, 0, 0, "")

    print("\n".join(brackets_sequences))


if __name__ == "__main__":
    main()
