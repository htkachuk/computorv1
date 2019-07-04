from my_math import sqrt


def solve_degree0(polinom):
    if polinom[0]["num"] == 0.0:
        print("All the real numbers are solution.")
    else:
        print("There are no solutions.")
    exit(0)


def solve_degree1(polinom):
    if len(polinom) == 1:
        print("All the real numbers are solution.")
        exit(0)
    c = 0
    b = 0
    for elem in polinom:
        if elem["pow_x"] == 0:
            c = elem["num"]
        if elem["pow_x"] == 1:
            b = elem["num"]
    print("The solution is:\n", -c / b)
    exit(0)


def solve_degree2(polinom):
    a = 0
    b = 0
    c = 0
    for elem in polinom:
        if elem["pow_x"] == 0:
            c = elem["num"]
        if elem["pow_x"] == 1:
            b = elem["num"]
        if elem['pow_x'] == 2:
            a = elem["num"]
    D = b * b - 4 * a * c
    if D < 0:
        print("Discriminant is negative, there are no solutions.")
        exit(0)
    if D == 0:
        return -b / 2 * a
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return x1, x2


def check_degree(degree, polinom):
    if degree == 0:
        return solve_degree0(polinom)
    if degree == 1:
        return solve_degree1(polinom)
    if degree == 2:
        return solve_degree2(polinom)


def solve_polinom(degree, polinom):
    answer = check_degree(degree, polinom)
    if len(answer) > 1:
        print(
            "Discriminant is strictly positive, the two solutions are:\n" + str(answer[0]) + "\n" + str(answer[1]))
    else:
        print("Discriminant is 0, solution is:\n" + str(answer))
