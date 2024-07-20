def separator(ls:list):
    z = []
    f = []
    for i in ls:
        if i%2 == 0:
            z.append(i)
        else:
            f.append(i)
    return(z,f)