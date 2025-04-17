m,n = map(int,input().split())
rows = []

for _ in range(m):
    rows.append(list(map(int, input().split())))

def col_sum(rows, c):
    return sum(rows[i][c] for i in range(m))  

col_sums_max = max(col_sum(rows, c) for c in range(n))
max_col_sum_index = next(c for c in range(n) if col_sum(rows,c)==col_sums_max)  #next(...) works with the generator expression and returns the first match....if we had put [] then it would  have returned all the indices and with max match and not just first one  

# max_sum_column_index = column_sums.index(max_column_sum)  ...for column_sums being a list and max_column_sum being the max value...IT WILL RETURN THE FIRST OCCURENCE OF IT! 

print(f'max col sum is {col_sums_max}')
print(f'max col sum index is {max_col_sum_index}')