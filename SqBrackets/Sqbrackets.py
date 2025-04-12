def surround_first_two_and_last_two_with_brackets(s: str):
    return (f'[{s[:2]}]{s[2:-2]}[{s[-2:]}]')

s = input('Enter the string: ')
print(surround_first_two_and_last_two_with_brackets(s))