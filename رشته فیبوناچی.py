n = int(input())


def fibonach(n):
    fn_1 = 1
    fn = 1
    output = []
    while fn <= n:
        output.append(fn)
        fn, fn_1 = fn + fn_1, fn
    return output


lst = fibonach(n)


for i in range(1, n + 1):
    print("+", end="") if i in lst else print("-", end="")
