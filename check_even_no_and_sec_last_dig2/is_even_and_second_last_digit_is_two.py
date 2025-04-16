def is_even_and_second_last_digit_is_two(n):
    return n%2 == 0 and str(n)[-2] == "2"     # NOTE: 2 must come in quotes because comparing with str

# or to check secondlast digit = 2.....abs(num)//10%10 ==2
# we added %10  above incase input integer is 3 digits or more

n = int(input())
print(is_even_and_second_last_digit_is_two(n))