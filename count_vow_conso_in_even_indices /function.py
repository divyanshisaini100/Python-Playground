import string 

#for alphabets and ascii char,remember this module

def count_vowels_and_consonants_in_even_indices(s : str) :
    # even_str = s[::2] can eliminate this line (MORE EFFICIENT)
    vowel = 0
    conso = 0
    for i in s[::2].lower():    #include lower() here so don't have to include again n again
        if i in 'aeiou':
            vowel += 1
        elif i in string.ascii_lowercase:  #or simply (w/o importing string)......... " i.isalpha() "....best for CHECK!(BEST HERE)
            conso += 1
        # else:
        #     pass  (NO NEED)
    return (vowel, conso)     

s = input()     
print(count_vowels_and_consonants_in_even_indices(s))