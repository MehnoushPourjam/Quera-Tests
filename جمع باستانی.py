fingers = int(input())
hands = int(input())
num1 = int(input())
num2 = int(input())

num_fingers = fingers*hands
nums = num2 + num1
if nums == 0:
    print(0)
elif nums%num_fingers == 0:
    print(num_fingers)
else:
    print(nums%num_fingers)