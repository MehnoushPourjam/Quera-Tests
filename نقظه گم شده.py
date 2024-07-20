x = []
y = []
z = []
for i in range(7):
    point = input().split()
    x.append(point[0])
    y.append((point[1]))
    z.append(point[-1])

x.sort()
y.sort()
z.sort()


x_ = x[0] if x.count(x[0]) == 3 else x[-1]
y_ = y[0] if y.count(y[0]) == 3 else y[-1]
z_ = z[0] if z.count(z[0]) == 3 else z[-1]


print(x_, y_, z_)
