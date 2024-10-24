print("Joel Gonsalves 111")
N = int(input("Enter the number of queens: "))
board = [[0] * N for i in range(N)]  

def is_attack(i, j):
  
    for k in range(N):
        if board[i][k] == "Q" or board[k][j] == "Q":  
            return True
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j): 
                if board[k][l] == "Q":
                    return True
    return False

def N_queen(n):
    if n == 0:
        return True  
    for i in range(N):
        for j in range(N):
            if not is_attack(i, j) and board[i][j] != "Q":
                board[i][j] = "Q"  
                if N_queen(n - 1):  
                    return True
                board[i][j] = 0  
    return False

N_queen(N)  
for row in board:
    print(row)
