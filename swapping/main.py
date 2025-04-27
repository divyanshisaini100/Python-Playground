# n = int(input())

# names = []

# for _ in range(n):
#     names.append(input())

# new= []
# for i in range(len(names)-1) :
#     if i > len(new):
#         new[i] =  names[i+1]
#         new[i+1] = names[i]
            
# for thing in new:
#     print(thing)  

n = int(input())
for i in range((n//2)):
    a, b = input(),input()
    print(b[::-1])
    print(a)
if n%2:
    print(input()[::-1])

