# def saghf(n):
#     if n-int(n) == 0:
#         return n
#     else:
#         return int(n)+1 if n >= 0 else (int(n))
#
#
# def caph(n):
#     if n-int(n) == 0:
#         return n
#     else:
#         return (int(n)-1) if n < 0 else int(n)
#
# def f(n):
#     if n == 1:
#         return 2
#     if n % 2 == 0:
#         return int(saghf((f(n-1))/2)*caph((f(n-1))/2))
#     else:
#         return int(f(n-1)-4)

def f(n):
    lst = [1, -3, 2, -2]
    if n == 1:
        return 2
    else:
        if n % 4 == 2:
            return lst[0]
        elif n % 4 == 3:
            return lst[1]
        elif n % 4 == 0:
            return lst[2]
        else:
            return lst[3]


answer = []
t = int(input())
for i in range(t):
    m = int(input())
    answer.append(f(m))

print(*answer, sep="\n")
