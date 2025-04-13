# This writes the stdin to the input file

# import tempfile
# import sys
# _, filename = tempfile.mkstemp(prefix="case")
# with open(filename, 'w') as f:
#     f.write(sys.stdin.read())


# Write your code to read the file and print the result.
# use the variable filename for the name of the file.

filename = input()

with open(filename) as f:
    lines = f.readlines()                      # returns list with \n like this: ['line1\n', 'line2\n', 'line3\n', 'line4']
    lines, ordering = lines[:-1], lines[-1].strip().split(",")  # strip to remove default '\n' in each line in 'lines' list
    ordered_lines = [lines[int(num) - 1] for num in ordering]   # TAKE TIME & PROCESS (NOTE: -1 is for indexing bcs python indexing is 0 based)
    print(*ordered_lines, sep = '') 
    
    # * SYmbol is "UNPACKING OPERATOR" so this way it prints out each line in list "ordered_lines" otherwise it will print whole LIST as it is !