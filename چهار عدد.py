n, a, b, c, d = map(int, input().split())

count = 0
for number in range(1 , n+1):
    if number % a == 0:
        count += 1
    elif number % b == 0:
        count += 1
    elif number %c == 0:
        count += 1
    elif number % d == 0:
        count += 1


print(count)