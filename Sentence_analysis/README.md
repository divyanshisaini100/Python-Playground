Write a function process_sentence(sentence, task) that analyzes a given sentence and computes the following according the task specified:

***count_words*** - Total number of words in the sentence.
***count_palindrome_words*** - Total number of palindrome words.
***count_words_with_repeated_chars*** - Total number of words that contain at least one repeated character.
***words_with_max_len*** - A set of longest words in the sentence (by number of characters).

**Assume words are seperated by spaces.**


**Examples**

1. count_words

>>> sentence = "level noon civic radar something"
>>> process_sentence(sentence,"count_words")
5
Explanation: There are 5 words in this sentence

2. count_palindromes

>>> sentence = "level noon civic radar something"
>>> process_sentence(sentence, "count_palindromes")
4
Explanation: "level", "noon", "civic" and "radar" are the palindromes

3. count_words_with_chars_repeated

>>> sentence = "hello world programming fun and interesting"
>>> process_sentence(sentence,"count_words_with_repeated_chars")
3
Explanation: "hello" (l is repeated), "programming" (m is repeated) and "interesting"(i, e, t and n are repated) has characters repeated

4. words_with_max_len

>>> sentence = "hello world programming fun and interesting"
>>> process_sentence(sentence, "words_with_max_len")
{'interesting', 'programming'}
Explanation: both the words 'interesting' and 'programming' has 11 characters which is the maximum number of characters in a word in the given sentence.