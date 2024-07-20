string = input()
count = 0
temp = 0


if len(string) == 1 and string == "0":
    count = 1
    print(count)
    quit()


for i in range(1, len(string)):
    if string[i] == "0":
        if string[i] == string[i-1]:
            count += 1
        else:
            count = 0

        temp = count+1 if temp<(count+1) else temp


print(temp)
