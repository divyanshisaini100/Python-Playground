# This writes the stdin to the input file

# import tempfile
# import sys
# _, filename = tempfile.mkstemp(prefix="case")
# with open(filename, 'w') as f:
#     f.write(sys.stdin.read())


# Write your code to read the file and print the result.
# use the variable filename for the name of the file.

with open('file.txt') as f:
    lines = f.readlines() 
    n = int(lines[0].strip())
    num = 1
    for line in lines[1:]:
        for char in line:
            if char == '_' and num<=n :
                char = str(num)
                num += 1    
            print(char, end = '')  
