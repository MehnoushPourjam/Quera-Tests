a = input().split()
b = input().split()

counter = 0

n = 7

while n >= 0:
    if a[n] == b[n] == "1":
        counter += 1
    n -= 1


print(counter)
