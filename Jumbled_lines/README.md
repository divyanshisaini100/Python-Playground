# Reorder the Jumbled Lines
Given a text file with several lines followed by a single line containing a comma-separated list of integers, reorder the lines of the text file based on the given order and print them.

The integers in the last line specify the new order of the preceding lines.
Each number corresponds to the position of a line (1-based index) in the original text.
Maintain the exact formatting and order as specified in the last line separated by comma.
NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

**Examples**

Input

first line 
second line 
third line
fourth line
1-3,2-4,3-2,4-1
Output

third line
fourth line
second line
first line