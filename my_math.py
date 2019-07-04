def sqrt(x):
    last_guess = x/2.0
    while True:
        guess = (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001:
            return guess
        last_guess = guess
