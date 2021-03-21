def ruler(a):
    i = 1
    s1 = ""
    s2 = " "
    while (i <= a):
        s1 += str(i % 10)
        i += 1
        if (i % 10 == 0):
            s2 += str(int(i / 10))
        else:
            s2 += " "
    print(s2)
    print(s1)

num = int(input("Give a number:  "))
ruler(num)