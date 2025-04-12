# Count Vowels and Consonants in Even Indices

Given a string s, count the number of vowels and consonants that appear at even indices in the string (0-based indexing). Ignore non-alphabetical characters.

Implement the **function count_vowels_and_consonants_in_even_indices** that returns the counts as described above.

The string s can have both upper and lower case letters.

Examples

"abcdeaeiou" -> (4, 1)
Characters at even indices are: 'a', 'c', 'e', 'e', 'u'.
Vowels: 'a', 'e', 'e', 'u' (4 vowels).
Consonants: 'c' (1 consonant).

"a11bc11de11" -> (2, 1)
Characters at even indices are: 'a', '1', 'b', '1', 'd', '1'.
Vowels: 'a' (1 vowel).
Consonants: 'b', 'd' (2 consonants).

"ABCDE" -> (2, 1)
Characters at even indices are: 'A', 'C', 'E'.
Vowels: 'A', 'E' (2 vowels).
Consonants: 'C' (1 consonant).