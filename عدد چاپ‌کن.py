string = input()

for number in string:
    p= ""
    for j in range(int(number)):
        p+= number

    print(number+":",p)