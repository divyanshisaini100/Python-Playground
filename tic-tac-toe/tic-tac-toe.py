

def diag_or_anti_diag(board):
    diag = []  
    anti_diag = []
    for i in range(len(board)):
        diag.append(board[i][i])    
        anti_diag.append(board[i][2-i])  #also board[i][-i-1] for anti_diag
    return [diag, anti_diag] 

def row(board, r):
    return board[r]

def col(board,c):
    col = []
    return col.append(board[i][c] for i in range(len(board))) 

def tic_tac_toe(board):
    patterns = []
    patterns.extend(diag_or_anti_diag(board))
    for i in range(len(board)):
        patterns.append(row(board,i))
        patterns.append(col(board,i))
    for pattern in patterns:
        if pattern == ['X']*3:
            return('X')
        if pattern == ['O']*3:
            return('O')
    return -1

# [['O','X','O'],['X','O','X'],['O','O','X']]

board = eval(input('ENTER THE BOARD: '))    
print(tic_tac_toe(board))



