n = int(input())


count = 0
temp = "1"
for i in range(n):
    places = input()
    if "1" in places and count == 0:
        for num in places.split():
            temp = num if num != "1" else temp
        count += 1
    elif places[0] == temp:
        temp = places[-1]


print(temp)
