a = int(input())
b = int(input())
c = int(input())
d = int(input())

lst = [a,b,c,d]


def average(lst:list):
    return sum(lst)/len(lst)

def product(lst:list):
    counter = 1
    for num in lst:
        counter *= num
    return counter

print(f"""Sum : {sum(lst):.6f}
Average : {average(lst):.6f}
Product : {product(lst):.6f}
MAX : {max(lst):.6f}
MIN : {min(lst):.6f}""", sep = "\n")