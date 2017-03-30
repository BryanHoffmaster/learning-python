import operator

_pedmas = ('(', '**', '*', '/', '+', '-')


def calc_add(arg1, arg2):
    return operator.add(arg1, arg2)


def calc_subtract(arg1, arg2):
    return operator.sub(arg1, arg2)


def calc_multiply(arg1, arg2):
    return operator.mul(arg1, arg2)


def calc_divide(arg1, arg2):
    try:
        return operator.truediv(arg1, arg2)

    except ZeroDivisionError as e:
        print(e)
        return 0


def parse_input(string1):
    num1 = 0.0
    num2 = 0.0

    math_dict = {"+": calc_add,
                 "-": calc_subtract,
                 "/": calc_divide,
                 "*": calc_multiply}

    for key in math_dict:
        if key in string1:
            string1.strip(' ')
            num1 = float(string1[:string1.index(key)])
            num2 = float(string1[string1.index(key) + 1:])
            return math_dict[key](num1, num2)
            # print("Answer: " + str(math_dict[key](num1, num2)) + "\n")
