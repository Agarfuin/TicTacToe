# Author: Harun Selman Karakas   2020
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

def game(turn):
	if turn % 2 == 0:
		player = "X"
		print("It's your turn " + player)
		move_place = input('')
		if move_place == theBoard[move_place]:
			theBoard[move_place] = "X"
			printBoard(theBoard)
			return 0
		else:
			print("You can not make this move.")
			printBoard(theBoard)
			game(turn)
	elif turn % 2 == 1:
		player = "O"
		print("It's your turn " + player)
		move_place = input('')
		if move_place == theBoard[move_place]:
			theBoard[move_place] = "O"
			printBoard(theBoard)
			return 0
		else:
			print("You can not make this move.")
			printBoard(theBoard)
			game(turn)

def win_conditions(turn):
	win_1 = theBoard["1"] == theBoard["2"] == theBoard["3"]
	win_2 = theBoard["4"] == theBoard["5"] == theBoard["6"]
	win_3 = theBoard["7"] == theBoard["8"] == theBoard["9"]
	win_4 = theBoard["1"] == theBoard["4"] == theBoard["7"]
	win_5 = theBoard["2"] == theBoard["5"] == theBoard["8"]
	win_6 = theBoard["3"] == theBoard["6"] == theBoard["9"]
	win_7 = theBoard["1"] == theBoard["5"] == theBoard["9"]
	win_8 = theBoard["3"] == theBoard["5"] == theBoard["7"]
	if turn % 2 == 0 and turn != 8:
		player = "X"
		if win_1 or win_2 or win_3 or win_4 or win_5 or win_6 or win_7 or win_8:
			print(f"*** CONGRATULATIONS {player} WON! ***")
			return 0
	elif turn % 2 == 1:
		player = "Y"
		if win_1 or win_2 or win_3 or win_4 or win_5 or win_6 or win_7 or win_8:
			print(f"*** CONGRATULATIONS {player} WON! ***")
			return 0
	elif turn == 8:
		print("*** IT'S A TIE! ***")
		return 0

def game_main():
	printBoard(theBoard)
	for i in range(9):
		if game(i) == 0:
			if win_conditions(i) == 0:
				break
			else:
				continue

if __name__ == "__main__":
	game_main()