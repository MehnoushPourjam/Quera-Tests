L, R = map(int,input().split())
string = "1"
while len(string) <= R:
    temp = ""
    for c in string:
        if c == "1":
            temp += "0"
        else:
            temp += "1"
    string += temp

print(string[L-1:R])