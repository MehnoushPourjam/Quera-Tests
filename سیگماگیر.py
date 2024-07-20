n = int(input())
m = int(input())

summ = 0
for i in range(-10, m+1):
    for j in range(1, n+1):
        summ += int(((i+j)**3)/(j**2))

print(summ)
