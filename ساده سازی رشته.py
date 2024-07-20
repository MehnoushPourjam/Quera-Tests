# n = int(input())
# string = input()
#
# new_string = [string[0]]
#
# i = 1
# # while i < n:
# #     if string[i] != string[i+1] and string[i] != string[i-1]:
# #         if new_string[len(new_string)-1] == string[i]:
# #             new_string.pop()
# #         else:
# #             new_string += string[i]
# #         i += 1
# #     else:
# #         if new_string[i-1] == string[i]:
# #             new_string.pop()
# #         i += 2
#
#
# while i < n:
#     if string[i] != string[i-1]:
#         if new_string[-1] == string[i]:
#             new_string.pop()
#         else:
#             new_string += string[i]
#     else:
#         new_string.pop()
#     i += 1
#
# print(*new_string, sep="")

# length_of_string = int(input())
# string = input()
#
# new_string = string[0]
#
# for letter in string[1:]:
#     if new_string[-1] != letter:
#         new_string += letter
#     else:
#         new_string = new_string[:(len(new_string)-1)]
#
#
#
# print(new_string)



length_of_string = int(input())
string = input()
string = [letter for letter in string]

lst = [string[0]]
for letter in string[1:]:
    if len(lst) != 0:
        if lst[-1] != letter:
            lst.append(letter)
        else:
            lst.pop()
    else:
        lst += [letter]




print(*lst, sep="")













