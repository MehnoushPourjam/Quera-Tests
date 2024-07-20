inpt = int(input())
lst = []
while inpt != 0:
    lst.append(inpt)
    inpt = int(input())

print(*list(reversed(lst)), sep = "\n")