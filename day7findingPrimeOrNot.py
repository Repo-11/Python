n = int(input("Check this number: "))


def prime_checker(number):
    num = 0
    for s in range(1, number + 1):
        p = (number) % s
        if p == 0:
            num = num + 1

    if num > 2:
        print("It's not a prime number")
    else:
        print("It's a prime number ")


prime_checker(n)

