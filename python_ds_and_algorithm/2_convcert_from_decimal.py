def convert_from_decimal(number:int, base:int)->int:
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10 
        number //= base
    return result


def test_convert_from_decimal():
    number, base = 9, 2
    assert convert_from_decimal(number, base) == 1001
    print('테스트 통과')

if __name__ == "__main__":
    test_convert_from_decimal()
