m, n = input().split()

def factoriel(n):
    if n == 1:
        return 1
    return n*factoriel(n-1)


string = str(factoriel(int(m)))
print(string.count(n))