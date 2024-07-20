m = int(input())
n = int(input())
x = 0
if m == 1 or n==1:
    x = m if n==1 else n
else:
    x = 2*m+(n-2)*2
print(x)