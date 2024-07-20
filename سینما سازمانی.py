n_officers ,k_cinema = map(int, input().split())

friends = list(map(int, input().split()))

friends.sort()

temp = 0
for num in friends:
    if k_cinema > 0 and num+1 <= k_cinema:
        k_cinema -= num+1
        temp += 1


print(temp)