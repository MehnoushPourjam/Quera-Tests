lst = []
for i in range(5):
    lst.append(input())

counter = []
for i,s in enumerate(lst):
    if "MOLANA" in s or "HAFEZ" in s:
        counter.append(i+1)

print("NOT FOUND!") if len(counter) == 0 else print(*counter)