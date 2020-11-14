'''
6.3
Dominos: There is an 8x8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominos, and a single domino can cover exactly two squares. Can you use the 31 dominos to cover the entire board? Prove your answer (by providing an example or showing why it's impossible).
'''

def dominos() -> list:
  chess_board = []
  print_board = []
  
  i = 0
  dom = 0
  while i < 64:
    if i == 0: 
      chess_board.append('cc')
    elif i == 63: 
      chess_board.append('cc')
    else:
      chess_board.append(dom)
    i += 1
    if i % 2 != 0: 
      dom += 1
    if i % 8 == 0:
      print_board.append(chess_board[i - 8: i])
  print(chess_board)
  
  j = 0
  while j < 7:
    if j % 2 != 0:
      print_board[j] = print_board[j][::-1]
    j += 1

  for row in print_board:
    print(row)
  
# # no crash
# ant 1 L
# ant 2 L
# ant 3 L
  
# ant 1 R
# ant 2 R
# ant 3 R

# # crash
# ant 1 R
# ant 2 L
# ant 3 L
  
# ant 1 R
# ant 2 R
# ant 3 L

# ant 1 L
# ant 2 R
# ant 3 R
  
# ant 1 L
# ant 2 R
# ant 3 L

dominos()