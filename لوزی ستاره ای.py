n = int(input())

i = (n-1)//2


for t in range(1,(n//2)+1):
    print(i*" "+(2*t-1)*"*"+2*i*" "+(2*t-1)*"*"+i*" ")
    i -= 1

i = 1
print((2*n)*"*")
n //= 2

while n > 0:
    print(i*" "+ (2*n-1)*"*" + 2*i*" "+ (2*n-1)*"*" + i*" ")
    n -= 1
    i += 1
