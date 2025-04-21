def is_positive_odd_or_negative_even(n):
    return (n%2 != 0 and n == abs(n)) or (n%2 == 0 and n != abs(n))

n = int(input())
print(is_positive_odd_or_negative_even(n))