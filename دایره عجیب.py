n, k = map(int, input().split())

if n == 1 or k == 1:
    print(1)
else:
    i = 1 + k
    counter = 1
    while i != 1:

        if i > n:
            i -= n

        if i == 1:
            break


        i += k
        counter += 1

    print(counter)
