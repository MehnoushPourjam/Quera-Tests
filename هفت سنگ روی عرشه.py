stones = input().split()
number = input()

temp = []
for i in range(len(stones)):
    if i == 0 and stones[0] == number:
        temp = stones[1:]
    elif i != 0 and stones[i] == number:
        temp = stones[i:]


print(len(temp))
