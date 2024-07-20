n = int(input())

def factoriel(m):
    if m == 1:
        return 1
    else:
        return m*factoriel(m-1)


print(factoriel(n))