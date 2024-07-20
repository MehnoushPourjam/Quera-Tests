n = int(input())
str1 = input()
str2 = input()
counter = 0
for i in range(n):
    if str2[i] != str1[i]:
        counter += 1

print(counter)