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
     

