def manage_time(x, y):
    time = x//y if x%y == 0 else (x//y)+1
    return time


k = int(input())
number_of_buildings = int(input())

buildings_highs = list(map(int, input().split()))

temp = buildings_highs[0]
time_counter = number_of_buildings + manage_time(temp, k)


for high in buildings_highs[1:]:
    if high > temp:
        time_counter += manage_time((high-temp), k)
    elif high < temp:
        time_counter += manage_time((temp-high), k)

    temp = high

time_counter += manage_time((buildings_highs[-1]), k)



print(time_counter)










