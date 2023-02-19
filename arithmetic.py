class Arithmetic:
    def __init__(self, a_type):
        if a_type not in ['INT','STRING']
            raise ValueError('Invalid arithmetic type)')



def main():
    import arithmetic_int, arithmetic_string

    a_string = arithmetic_string.ArithmeticString()
    a_int = arithmetic_int.ArithmeticInt()

    res = a_string.add(3,4)
    print(res, type(res))

    res = a_int.add(3,4)
    print(res, type(res))



if __name__ == '__main__':
    main()