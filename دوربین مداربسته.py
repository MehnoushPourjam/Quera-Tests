x1, y1 = map(int,input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xs = [x1, x2, x3]
ys = [y1, y2, y3]

xs.sort()
ys.sort()

if xs[0] == xs[1]:
    x4 = xs[-1]
else:
    x4 = xs[0]


if ys[0] == ys[1]:
    y4 = ys[-1]
else:
    y4 = ys[0]


print(x4, y4)