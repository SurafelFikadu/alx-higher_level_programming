i = 0
while i <= 89:
    if i % 10 == 0:
        i += 1 + i // 10
    if i < 89:
        print("{:02d}".format(i), end=", ")
    else:
        print(i)
    i += 1
