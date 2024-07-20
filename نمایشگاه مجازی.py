k = int(input())

#
# lst = [
#     '########.......########',
#     '#ghorfe1.......ghorfe2#',
#     '########.......########',
#     '#.....................#',
#     '########.......########',
#     '#.....................#',
#     '########.......########',
#     '#.....................#',
#     '#######################',
# ]


if k%2 ==0:
    n = 1
    lst = []
    while n <= k//2:
        lst.append(f"#ghorfe{(2*n)-1}.......ghorfe{n*2}#")
        n += 1
    i = 1
    for l in range(8):
        if l%2 == 0:
            print('########.......########')
        else:
            try:
                print(lst[i-1])
                i += 1
            except:
                print('#.....................#')
else:
    n = 1
    lst = []
    while n <= k:
        lst.append(f"ghorfe{n}")
        n += 1
    i = 0
    for l in range(8):
        if l%2 == 0:
            print('########.......########')
        else:
            try:
                for j in range(3):
                    if j == 0:
                        print("#"+lst[i],end="")
                    elif j == 1:
                        print(".......", end = "")
                    else:
                        print(lst[i+1]+"#")
            except:
                if j == 0:
                    print('#.....................#')
                elif j == 2:
                    print(".......#")
            i += 2

print('#######################')