n = int(input())

officer = []
mmax = 0
for i in range(n):
    name, money = input().split()
    money = int(money)
    if money > mmax:
        mmax = money
    officer.append([name, money])


for i, j in officer:
    if j == mmax:
        print(i)
        break
