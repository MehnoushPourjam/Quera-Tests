string = input()
counter = 0

for letter in string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        counter += 1


print(2**counter)