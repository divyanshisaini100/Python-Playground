def is_positive_odd_or_negative_even(n):
    return (n%2 != 0 and n == abs(n)) or (n%2 == 0 and n != abs(n))
    #return (n % 2 != 0 and n > 0) or (n % 2 == 0 and n < 0)     MORE EFFICIENT
    
n = int(input())
print(is_positive_odd_or_negative_even(n))
