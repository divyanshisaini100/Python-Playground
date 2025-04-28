
    

def continuous(words):
    new_list = []
    for word in words:
        if word.lower().endswith("ing"):
            new_list.append(word)  
    return new_list

def vowel_rich(words):
    new_list = []
    for word in words:
       count =0
       for letter in word.lower():
           if letter in "aeiou":
               count += 1 
       if count >5:
           new_list.append(word)   
    return new_list

def consonant_rich(words):
    new_list = []
    for word in words:
        count = 0
        for letter in word.lower():
            if letter not in "aeiou" and letter.isalpha():
                count += 1
        if count > 5:
            new_list.append(word)
    return new_list 

def is_sorted(words):
    new_list = []
    for word in words:
        if list(word) == sorted(word): 

#sorted(word) returns a list of characters, not a string.
# But word is a string.
# So you are comparing a string with a list — they will never be equal.

            new_list.append(word)
    return new_list

def get_words_by_criteria(words, criteria=None):
    """
    Filters words based on the given criteria.

    Args:
        words (list): List of words.
        criteria (str): The filter criteria.

    Returns:
        list: Filtered list of words matching the criteria, or None if invalid criteria.
    """

    if criteria == "continuous":
        return continuous(words)
    elif criteria == "vowel_rich":
        return vowel_rich(words)
    elif criteria == "consonant_rich":
        return consonant_rich(words)
    elif criteria == "sorted":
        return is_sorted(words)
    else:
        return None