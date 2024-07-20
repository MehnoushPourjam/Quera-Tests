chocolates = list(map(int, input().split()))

members = [0, 0, 0, 0]

def cho(items: list):
    items += [items.pop(0)]
    return items


j = 0
while 0 not in chocolates:
    members[j] += 1
    chocolates[j] -= 1

    chocolates = cho(chocolates)

    if j == 3:
        j = 0
    else:
        j += 1

print(*members)
