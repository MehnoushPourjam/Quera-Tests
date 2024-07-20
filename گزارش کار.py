n, k = map(int, input().split())

cs = []
for i in range(n):
    cs.append(int(input()))


if sum(cs) >= k:
    print("YES")

else:
    print("NO")