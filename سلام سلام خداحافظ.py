n = int(input())
names = input().split()

salam = [names[0]]
for i in range(1,n):
    for person in salam:
        print(names[i]+":",f"salam {person}!")
    salam.insert(0,names[i])


for i in range(n):
    print(names[0]+":","khodafez bacheha!")
    name = names[0]
    names.pop(0)
    for person in names:
        print(f"{person}: khodafez {name}!")


