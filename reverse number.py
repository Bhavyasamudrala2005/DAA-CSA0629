def reverse_number(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        reversed_remaining = reverse_number(n // 10)
        reversed_number = int(str(last_digit) + str(reversed_remaining))
        return reversed_number
number = 12345
print("Original number:", number)
print("Reversed number:", reverse_number(number))
