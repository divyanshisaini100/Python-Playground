def last_word_starts_with_upper_case(sentence: str):
    """
    Find the last word in a sentence that starts with an uppercase letter.

    Args:
        sentence (str): The input sentence.

    Returns:
        str or None: The last word starting with an uppercase letter, or None if no such word exists.
    """
    
    for word in s.split():
        if word[0].isupper():                  ###### NOTE the syntax is : " .isupper()"
            return word
    return None  