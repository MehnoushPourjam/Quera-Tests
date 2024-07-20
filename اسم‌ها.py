n = int(input())

names = []

for i in range(n):
    name = input()
    charecters = []
    for letter in name:
        if letter not in charecters:
            charecters.append(letter)

    names.append(len(charecters))


names.sort()

print(names[-1])