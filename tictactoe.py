# -*- coding: utf-8 -*-

theBoard = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

def zero_to_infinity():
    j = 0
    while True:
        yield j
        j += 1

def printBoard(board):
  print(board['1'] + '|' + board['2'] + '|' + board['3'])
  print('-+-+-')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('-+-+-')
  print(board['7'] + '|' + board['8'] + '|' + board['9'])

def move(turn):
  if turn % 2 == 0:
    player = "X"
    print("It's your turn " + player)
  elif turn % 2 != 0:
    player = "O"
    print("It's your turn " + player)
  move_place = str(input())
  if player == "X":
    if theBoard[move_place] == "X" or theBoard[move_place] == "O":
      print("That place already taken, you can not make this move.")
      return 0
    else:
      theBoard[move_place] = "X"
      return 1
  elif player == "O":
    if theBoard[move_place] == "X" or theBoard[move_place] == "O":
      print("That place already taken, you can not make this move.")
      return 0
    else:
      theBoard[move_place] = "O"
      return 1

def winner_tie_message(turn):
  case_1 = theBoard["1"] == theBoard["2"] == theBoard["3"]
  case_2 = theBoard["4"] == theBoard["5"] == theBoard["6"]
  case_3 = theBoard["7"] == theBoard["8"] == theBoard["9"]
  case_4 = theBoard["1"] == theBoard["4"] == theBoard["7"]
  case_5 = theBoard["2"] == theBoard["5"] == theBoard["8"]
  case_6 = theBoard["3"] == theBoard["6"] == theBoard["9"]
  case_7 = theBoard["1"] == theBoard["5"] == theBoard["9"]
  case_8 = theBoard["3"] == theBoard["5"] == theBoard["7"]
  if turn % 2 == 0:
    player = "X"
  elif turn % 2 != 0:
    player = "O"
  if case_1 or case_2 or case_3 or case_4 or case_5 or case_6 or case_7 or case_8:
    printBoard(theBoard)
    print(f"*** CONGRATULATIONS {player} WON! ***")
    return 0
  else:
    return 1
  
def game_main():
  for i in zero_to_infinity():
    printBoard(theBoard)
    while True:
      if move(i) == 1:
        break
      elif move(i) == 0:
        continue
    if winner_tie_message(i) == 0:
      break
    elif i == 8:
      printBoard(theBoard)
      print("*** IT'S A TIE! ***")
      break

if __name__ == "__main__":
  game_main()