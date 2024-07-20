lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))


counter = 0
for j in range(1,n):
    if lst[j] != lst[j-1]:
        counter += 1

print(counter)