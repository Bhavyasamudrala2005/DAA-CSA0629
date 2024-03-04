def print_pattern(n):
    if n == 0:
        return
    print_pattern(n - 1)
    for i in range(1, n + 1):
        print(i, end="")
    print()
rows = 5
print("Pattern")
print_pattern(rows)
