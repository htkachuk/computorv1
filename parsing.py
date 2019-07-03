def add_symbol(sub, symb):
    if (sub[0] != '-' and sub[0] != '+'):
        sub = symb + sub
    return sub


def check_sub(polinom, sub, symb):
    if sub != '':
        sub = add_symbol(sub, symb)
        polinom.append(sub)
    return polinom


def parse(polinom, input_str, i):
    sub = ''
    i += 1
    k = 0

    while i < len(input_str):
        if input_str[i] == '+' and i != 0:
            sub = add_symbol(sub, '-')
            polinom.append(sub)
            sub = '-'
            k = 1
            i += 1
        if input_str[i] == '-' and i != 0:
            sub = add_symbol(sub, '-')
            if sub[0] != '+' and sub[0] != '-':
                '-' + sub
            polinom.append(sub)
            sub = '+'
        sub += input_str[i]
        i += 1

    return check_sub(polinom, sub, '-')


def parse_polinom(polinom):
    polinom_array = []

    for elem in polinom:
        param = {}
        num_ready = False
        num = ''
        for c in elem:
            if c == '+' or c == '-':
                sign = c
            if (c == '.' or c == ',') and num_ready == False:
                num += '.'
            if c.isnumeric():
                if num_ready == False:
                    num += c
                else:
                    if sign == '-':
                        num = '-' + num
                    param["num"] = float(num)
                    param["pow_x"] = int(c)
                    polinom_array.append(param)
            if c == 'X':
                num_ready = True

    return polinom_array


def parse_input(input_str):
    polinom = []
    i = 0
    sub = ''

    while input_str[i] != '=':
        if (input_str[i] == '+' or input_str[i] == '-') and (i != 0):
            sub = add_symbol(sub, '+')
            polinom.append(sub)
            sub = ''
        sub += input_str[i]
        i += 1

    if input_str[i] != '=':
        return None, Error

    polinom = parse(check_sub(polinom, sub, '+'), input_str, i)
    return parse_polinom(polinom), None
