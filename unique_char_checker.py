def has_unique_chars(s):
    s_list = [x for x in s.lower()]
    s_set = set(s_list)
    return len(s_list) == len(s_set)

s = input()
print(has_unique_chars(s))   