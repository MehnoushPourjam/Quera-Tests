def is_prime(m):
    if m == 1:
        return False
    elif m == 2 or m == 3:
        return True
    else:
        for i in range(2,1+(m//2)):
            if m%i == 0:
                return False
    return True


a = int(input())
b = int(input())

lst = []
for i in range(a+1,b):
    if is_prime(i):
        lst.append(i)



print(*lst,sep=",")