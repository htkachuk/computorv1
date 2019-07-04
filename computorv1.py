import sys
from copy import deepcopy

from parsing import parse_input
from reduced_form import make_reduced, reduced_string, polinom_degree
from solving import solve_polinom


def main():
    parse_input(sys.argv[1])
    try:
        polinom, err = parse_input(sys.argv[1])
    except:
        print("Error")
    if (err != None):
        print(err)
        exit()
    degree = polinom_degree(polinom)
    reduced_form, err = make_reduced(polinom, degree)
    if (err != None):
        print(err)
        exit()
    print("Reduced form: " + reduced_string(deepcopy(reduced_form), degree))
    print("Polynomial degree: " + str(degree))
    if degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        exit()
    solve_polinom(degree, reduced_form)


if __name__ == "__main__":
    main()
