def Fard(n):
    if n%2 == 0:
        return False
    return True


def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or  n == 3:
        return True
    else:
        for num in range(2, n//2):
            if n%num == 0:
                return False

    return True

m = int(input())

print("zoj" if Fard(m) == True and is_prime(m) == True else "fard")