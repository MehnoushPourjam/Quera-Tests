n = int(input())
per = input().split()
num = input().split()

counter = 0
for i in range(n):
    counter += int(per[i])*int(num[i])


print(counter)