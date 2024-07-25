from math import sqrt

n = int(input())


def sum_digit(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ


def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, (n//2)+ 1):
            if n % i == 0:
                return False
    return True


b = sum_digit(n)
counter = 1
n+=1
while b>0:
    if is_prime(n):
        counter = n
        b-=1
    n += 1

print(counter)
