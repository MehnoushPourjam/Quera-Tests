mohreh = input().split()

lst = [1,1,2,2,2,8]
result = []

for i in range(6):
    if int(mohreh[i]) == lst[i]:
        result.append(0)
    else:
        result.append(lst[i]-int(mohreh[i]))


print(*result)