a, b, c = map(int,input().split())
if (a != 0 and b != 0 and c != 0) and (a != 180 and b != 180 and c != 180):
    print("YES") if a + b + c == 180 else print("NO")
else:
    print("NO")