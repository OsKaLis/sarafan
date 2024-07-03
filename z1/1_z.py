def sequence_n(number: int) -> str:
    """
    1.	Напишите программу, которая выводит n первых элементов
    последовательности 122333444455555…
    (число повторяется столько раз, чему оно равно).
    """
    rez: str = ''
    for value in range(1, number+1):
        rez += str(value)*value
    return rez


if __name__ == "__main__":
    assert sequence_n(5) == '122333444455555'
    assert sequence_n(3) == '122333'
    assert sequence_n(9) == '122333444455555666666777777788888888999999999'
