n_watermelons = int(input())

w = map(int,input().split())

weighs = []
a = 0
for m in w:
    weighs.append([a, m])
    a += 1

while len(weighs) != 1:
    if weighs[1][1] < weighs[0][1]:
        weighs.remove(weighs[1])
    else:
        weighs.remove(weighs[0])






print(weighs[0][0]+1)