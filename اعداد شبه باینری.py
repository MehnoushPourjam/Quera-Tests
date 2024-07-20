m = int(input())


def divisor(n):
    sum = 0

    for i in range(1, 1+(n//2)):
        if n % i == 0:
            sum += i

    return sum


def is_binary(n):
    for i in range(0, 14):
        if 2**i == n:
            return print(1)
    else:
        return print(0)




is_binary((divisor(m)))

