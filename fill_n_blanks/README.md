# Fill the first n blanks with 1 to n
Write a program to fill the first n blanks (represented by underscores _) in a text with numbers from 1 to n.

The first line of the input contains the integer n, the number of blanks to fill.
Subsequent lines contain the text, with blanks represented as _.
Fill the blanks sequentially with numbers from 1 to n.
If there are more blanks than n, the remaining blanks remain unchanged.

NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

**Example**

***Input***

11
a_bc__d___e
f_g__h__i__j
k___l_m__n

***Output***

11
a1bc23d456e
f7g89h1011i__j
k___l_m__n