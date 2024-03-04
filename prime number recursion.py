def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)
def print_primes_recursive(start, end):
    if start <= end:
        if is_prime(start):
            print(start, end=" ")
        print_primes_recursive(start + 1, end)
start_num = 2
end_num = 50
print("Prime numbers between", start_num, "and", end_num, "are:")
print_primes_recursive(start_num, end_num)
