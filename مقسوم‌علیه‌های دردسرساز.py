def divisor(n):
    counter = 0
    summ = 0
    for i in range(1,n+1):
        if n % i == 0:
            counter += 1
            summ += i
    return counter, summ


n = int(input())
summ = 0
counter = 0
for i in range(1,n+1):
    j, k = divisor(i)
    summ += k
    counter += j

print(counter, summ)
