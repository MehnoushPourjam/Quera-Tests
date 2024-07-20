n, m =map(int,input().split())
counter = 0
for N in range(n):
    inpt = input()
    for c in inpt:
        if c == "*":
            counter += 1


print(counter)