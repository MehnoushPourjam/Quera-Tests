mouse, home = map(int, input().split())

if mouse == home:
    print("Saal Noo Mobarak!")

else:
    if home>mouse:
        print("R"*(home-mouse))
    else:
        print("L"*(mouse-home))