for i in range(1, 6):
    if i == 1:
        print("*")
    elif i == 5:
        print("* " * 5)
    else:
        print("*" + " " * (2 * i - 2) + "*")