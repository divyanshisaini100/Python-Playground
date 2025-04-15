def replace_vowels_with_next_alphabet(s: str) -> str:
    """
    Replaces all vowels in the input string with the next character in the alphabet.

    Args:
        s (str): The input string to process.

    Returns:
        str: A string with all vowels replaced by their next alphabetical character.
    
    Note:
        This function is case-sensitive.
    
    Examples:
        >>> replace_vowels_with_next_alphabet("hello")
        'hflmp'
        >>> replace_vowels_with_next_alphabet("HELLO")
        'HFLMP'
    """
    result = ''
    for char in s:        
        if char in 'aeiouAEIOU':
            char = chr(ord(char)+1)  # NOTE: ord & chr function
        result += char               # printing inside function is not recommended 'print(char,end='') scatters the logic and prints outside also print(to call def) shows error! Better to collect the string char in a'str'or'list'
    return result     

s = input()
print(replace_vowels_with_next_alphabet(s))        

#🧨 Problem 1: You're printing inside the function — not returning the result
# You're doing:

# python
# Copy
# Edit

# for char in s:
#     ...
#     print(char, end='')

# But then you also call:

# python
# Copy
# Edit
# print(replace_vowels_with_next_alphabet(s))
# Which prints None at the end — because your function doesn’t return anything, so replace_vowels_with_next_alphabet(s) evaluates to None.

# 🧨 Problem 2: You're printing each character individually — instead of building a string
# That makes the logic scattered and hard to reuse. Better to collect modified characters in a string or list and return it.

