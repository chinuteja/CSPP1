# def isvalidinput(board):
#     sum = 0
#     x_sum = 0
#     o_sum = 0
#     for i in board:
#         x_sum += i.count("x")
#         o_sum += i.count("o")
#         dot_sum += i.count(".")
#         sum +=i.count("x") + i.count("o") + i.count(".")
#     if sum != 9:
#         print("invalid input")
#         return 
#     if (x_sum - o_sum not in (0,1,-1) or ((x_sum == dot_sum) and (o_sum == dot_sum))):
#         print("invalid game")
#         return
#     #else:
#         #print("invalid input")
#     return True

# def check_horizontal(board):
#     for i in range(len(board)):
#         if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
#             return board[i][0]
# def check_vertical(board):
#     for i in range(len(board)):
#         if board[0][i] == board[1][i] and board[2][i] == board[1][i]:
#             return board[0][i]
# def check_diagonal(board):
#     if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
#         return board[0][0]
#     if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
#         return board[0][2]
# def checkwinner(board):
#     winner = check_horizontal(board)
#     if winner:
#         return winner
#     winner = check_vertical(board)
#     if winner:
#         return winner
#     winner = check_diagonal(board)
#     if winner:
#         return winner
#     else:
#         return "draw"
# def main():
#     board = []
#     for i in range(3):
#         board.append(input().split())
#     if isvalidinput(board):
#         #print(board)
#         print(checkwinner(board))
def Tic_Tac_Toe(matrix):
   winner = []
   for row in matrix:
       if row[0] == row[1] == row[2]:
           winner.append(row[0])
   for i in range(0,3):
       if matrix[0][i] == matrix[1][i] == matrix[2][i]:
           winner.append(matrix[0][i])
   if matrix[0][0] == matrix[1][1] == matrix[2][2]:
           winner.append(matrix[0][0])
   if matrix[2][0] == matrix[1][1] == matrix[0][2]:
       winner.append(matrix[0][2])
   if len(winner) == 0:
       print('draw')
       return None
   if len(winner) == 1:
       if winner[0] == 'x' or winner[0] == 'o':
           print(winner[0])
       else:
           print("invalid input")
       return winner[0]
   else:
       print("invalid game")
       return None
def main():
   matrix = []
   for _ in range(0, 3):
       col = input().split(' ')
       matrix.append(col)
   Tic_Tac_Toe(matrix)
if __name__ == '__main__':
   main()