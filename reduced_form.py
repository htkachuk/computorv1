def make_reduced(polinom, degree):
    polinom_array = []
    err = None

    for i in range(degree + 1):
        param = {}
        num = 0
        for elem in polinom:
            param["pow_x"] = i
            if elem["pow_x"] > 2:
                err = "Polinom pow array!"
            if elem["pow_x"] == i:
                num += elem['num']
        param["num"] = num
        polinom_array.append(param)

    return polinom_array, err


def reduced_string(polinom, degree):
    output_str = ''

    for i in range(degree + 1):
        for elem in polinom:
            if elem["pow_x"] == i:
                if int(elem['num']) == elem['num']:
                    elem['num'] = int(elem['num'])
                if i != 0:
                    if elem['num'] > 0:
                        output_str += "+ "
                    else:
                        elem['num'] *= -1
                        output_str += "- "
                output_str += str(elem['num']) + ' * X^' + str(i) + " "
    output_str += "= 0"
    return output_str


def polinom_degree(polinom):
    degree = 0

    for elem in polinom:
        if degree < elem['pow_x']:
            degree = elem['pow_x']

    return degree
