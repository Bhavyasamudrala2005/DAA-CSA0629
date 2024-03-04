def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n
number = 28
print(number, "a perfect number", is_perfect_number(number))
