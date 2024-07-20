
def calculate_floor(string):
    temp = 0
    for car in string:
        if car == "U":
            temp += 1
        else:
            temp -= 1

    return temp
