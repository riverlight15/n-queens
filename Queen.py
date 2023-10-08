import numpy as np


all_positions = 0
n = int(input("n = "))
board = np.zeros((n, n), dtype = int)

def placeQueen(i, j):
    for q in range(n):
        board[q][j] += 1
        board[i][q] += 1
        L_R = i+j-q
        R_L = i-j+q
        if 0 <= L_R < n:
            board[L_R][q] += 1
        if 0 <= R_L < n:
            board[R_L][q] += 1
    board[i][j] = -1


def removeQueen(i, j):
    for q in range(n):
        board[q][j] -= 1
        board[i][q] -= 1
        L_R = i+j-q
        R_L = i-j+q
        if 0 <= L_R < n:
            board[L_R][q] -= 1
        if 0 <= R_L < n:
            board[R_L][q] -= 1
    board[i][j] = 0

def getPosition():
    result = []
    column = "abcdefgh"
    global all_positions
    all_positions += 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                result.append(column[j] + str(i+1))
    print(", ".join(result))

def main(i):
    if 1 < n < 4:
        print("Нет решений")
        exit(0)
    else:
        for j in range(n):
            if board[i][j] == 0:
                placeQueen(i, j)
                if i == n-1:
                    getPosition()
                else:
                    main(i+1)
                removeQueen(i, j)

main(0)
print(all_positions)