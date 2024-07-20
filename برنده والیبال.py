t = int(input())

sets = []
temp = []
for i in range(t):
    temp.append(input())
    temp.append(input())
    sets.append(temp[-1])

    temp.clear()

result = []
for j in sets:
    Q = j.count("Q")
    C = j.count("C")
    result.append("CodeCup" if C > Q else "Quera")


print(*result, sep='\n')

