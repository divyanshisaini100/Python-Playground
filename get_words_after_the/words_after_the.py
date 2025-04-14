def get_words_after_the(sentence: str) -> list:
        
    words = sentence.split()
    lst = []
    for i in range(len(words)):
        if words[i].lower() == 'the' and (i+1) in range(len(words)):
            lst.append(words[i+1])
    return lst

sentence = input()
print(get_words_after_the(sentence))

# OTHER WAY (PROBABLY MORE EFFICIENT) :

def get_words_after_the1(sentence: str) -> list:

    words = sentence.split()
    words_after_the = []
    for i in range(1, len(words)):
       if words[i - 1].lower() == 'the':
           words_after_the.append(words[i])
    return words_after_the

