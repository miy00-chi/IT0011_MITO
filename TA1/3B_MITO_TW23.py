def pattern_b(n):
    i = 1
    while i <= n:
        if i % 2 != 0:  # Print only for odd numbers
            print(str(i) * i)
        i += 1

# Example usage
pattern_b(7)