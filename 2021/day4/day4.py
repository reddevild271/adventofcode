from sys import stdin

numbers = stdin.readline().split(',')

boards = []

for line in stdin:
  if line == '\n':
    boards.append([])
    continue
  boards[-1].append(line.split())
  
def board_check( board, numbers ):
  for i in range(5):
    if board[i][i] in numbers:
      result = True
      for j in range(1,5):
        if board[i][(i+j)%5] not in numbers:
          result = False
          break
      if result:
        return True
      result = True
      for j in range(1,5):
        if board[(i+j)%5][i] not in numbers:
          result = False
          break
      if result:
        return True
  return False

def unmarked_sum( board, numbers ):
  result = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] not in numbers:
        result += int(board[i][j])
  return result

first_board = True
next_boards = []
for i in range(5, len(numbers)):
  for board in boards:
    if board_check( board, numbers[:i] ):
      if first_board:
        print( 'Part 1: ' + str(unmarked_sum( board, numbers[:i] ) * int(numbers[i-1])) )
        first_board = False
      elif len(boards) == 1:
        print( 'Part 2: ' + str(unmarked_sum( board, numbers[:i] ) * int(numbers[i-1])) )
        raise SystemExit
    else:
      next_boards.append(board)
  boards = next_boards
  next_boards = []
      
