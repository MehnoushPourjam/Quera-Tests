day = input()
days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

list_of_crimes = [int(input()) for n in range(30)]

def recognizing_the_day(d):
    lst = days[days.index(d):]
    if len(lst) != 7:
        lst += days[:days.index(d)]
    return lst


result = []

for j,da in enumerate(recognizing_the_day(day)):
    summ = 0
    counter = 0
    for nums in list_of_crimes[j::7]:
        summ += nums
        counter += 1


    result.append((summ/counter, da))


result.sort()
print(result[0][-1], int(result[0][0]))