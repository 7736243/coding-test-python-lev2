while 1:
    a = input()
    if a=="0":
        break;
    else:
        b = "".join(reversed(a))
        if a==b:
            print("yes")
        else:
            print("no")