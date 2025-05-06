# n = 3
# \ /
#  x
# / \

# n=1
# x

# n=5
# \   /
#  \ /
#   x
#  / \
# /   \ 

n = int(input('Enter an odd number: '))

for i in range(1,n//2):
    print((i-1)*' ' + '\\' + ' '*(5-i*2)+'/')
print(' '*(n//2) + 'x') 
for i in range(1,n//2):
    print((i-1)*' ' + '/' + ' '*(5-i*2)+'\\') 


    #USING ONLY SLASHES AND SPACES     
for i in range(n):
    for j in range(n):
        if i == j and j == n // 2:
            print("x", end="")  # center
        elif j == i:
            print("\\", end="")
        elif j == n - i - 1:
            print("/", end="")
        else:
            print(" ", end="")
    print()



