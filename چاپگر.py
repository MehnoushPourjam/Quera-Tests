n, m = map(int,input().split())

def print_the_objects(shape:str, tool:int):
    if shape == ".":
        for i in range(1, 4):
            if i % 2 == 1:
                print("." * tool, end="")
            else:
                print("X" * tool, end="")
        print()

    else:
        for i in range(1,4):
            if i%2 == 1:
                print("X"*tool, end="")
            else:
                print("."*tool, end="")
        print()


for rectangle in range(1,4):
    if rectangle%2 == 1:
        for j in range(1, n+1):
            print_the_objects("X", m)
    else:
        for k in range(1, n+1):
            print_the_objects(".", m)