n = int(input())

word = ''
for i in range(n):
    s = input()
    if i % 2 == 0:
        word = word + s
    else:
        word = s + word
print(word)

#____________________________USING LIST___________________________

# word = []
# for i in range(n):
#     s = input()
#     if i%2 == 0:
#         word.append(s)
#     else:
#         word.insert(0,s)     # NOTE: .insert(index, element)  ....used when wanna insert into list at custom place ("append", "extend" works well for inserting at last)
# print(''.join(word))         # NOTE: ''.join() syntax