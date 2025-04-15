def is_even_and_second_last_digit_is_two(n):
    return n%2 == 0 and str(n)[-2] == "2"     # NOTE: 2 must come in quotes because comparing with str

n = int(input())
print(is_even_and_second_last_digit_is_two(n))