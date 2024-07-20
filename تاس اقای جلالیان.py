n = int(input())

lst = [
    [1, 6],
    [2, 5],
    [3, 4]
       ]


for i in lst:
    if n in i:
        print(i[1] if i[0] == n else i[0])