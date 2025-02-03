def pattern_b(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(str(i) * i)
        i += 1
pattern_b(7)
