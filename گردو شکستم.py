n, x, y= map(int,input().split())

if n%x == 0:
    print(n//x, 0)
    quit()
elif n%y == 0:
    print(0, n//y)
    quit()
else:
    i = 1
    while n-(x*i)>0:
        if (n-(x*i))%y == 0:
            print(i, (n-(x*i))//y)
            quit()
        i+= 1

    i = 0
    while n - (y * i) > 0:
        if (n - (y * i)) % x == 0:
            print((n - (y * i))//x, i)
            quit()
        i += 1



print("-1")