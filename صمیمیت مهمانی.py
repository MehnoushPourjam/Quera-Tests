n = int(input())
lst = input().split()
mmax = 0
for num in lst:
    if mmax<int(num):
        mmax = int(num)

print(round(mmax/1, 6))