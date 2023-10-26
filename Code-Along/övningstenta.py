def pattern(n):
    for i in range(n):
        if i % 2 == 0:
            row = "x " * n
        else:
            row = "x o x o x"
        print(row)

pattern(5)


