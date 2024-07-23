string = input()

if string.count("R") >= 3:
    print("nakhor lite")
elif string.count("R") >= 2 and string.count("Y") >= 2:
    print("nakhor lite")
elif "G" not in string:
    print("nakhor lite")
else:
    print("rahat baash")
