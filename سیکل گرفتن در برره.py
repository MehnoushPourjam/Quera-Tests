N = int(input())
keys = input()


def keyvan(N: int, key: str):
    counter = 0
    for i in range(1, N + 1):
        if (i % 6 == 1 or i % 6 == 2) and key[i - 1] == "3":
            counter += 1
        elif (i % 6 == 3 or i % 6 == 4) and key[i - 1] == "1":
            counter += 1
        elif (i % 6 == 5 or i % 6 == 0) and key[i - 1] == "2":
            counter += 1
    return counter


def nezam(N: int, key: str):
    counter = 0
    for i in range(1, N + 1):
        if i % 3 == 1 and key[i - 1] == "1":
            counter += 1
        elif i % 3 == 2 and key[i - 1] == "2":
            counter += 1
        elif i % 3 == 0 and key[i - 1] == "3":
            counter += 1
    return counter


def shir_farhad(N: int, key: str):
    counter = 0
    for i in range(1, N + 1):
        if (i % 4 == 1 or i % 4 == 3) and key[i - 1] == "2":
            counter += 1
        elif i % 4 == 2 and key[i - 1] == "1":
            counter += 1
        elif i % 4 == 0 and key[i - 1] == "3":
            counter += 1
    return counter


counts = [keyvan(N, keys), nezam(N, keys), shir_farhad(N, keys)]
lst = [("keyvoon", keyvan(N, keys)), ("nezam", nezam(N, keys)), ("shir farhad", shir_farhad(N, keys))]
print(max(counts))
for name,score in lst:
    if max(counts) == score:
        print(name)