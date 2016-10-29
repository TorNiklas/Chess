board_string  = "RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
change_string = "RNBQKBN.PPPPPPPp................................Pppppppp.nbqkbnr"
move_string   = "RNBQKBNRP..............................................prnbqkbnr"
board = [["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10,["0"]*10]
current_legal_moves = []
white_pieces = ["R", "N", "B", "Q", "K", "P"]
black_pieces = ["r", "n", "b", "q", "k", "p"]
white = True


def make_board(board_string):
	l = list(board_string)

	index  = 0
	for i in range(1,9):
		for j in range(1,9):
			if (l[index] == "."):
				board[i][j] = None
			else:
				board[i][j] = l[index]
			index += 1
def present_board():
	print("_________________________________")
	for i in range(8, 0, -1):
		row = "|"
		for j in range(1, 9):
			if (board[i][j] == None):
				row += "   |"
			else:
				row += " " + board[i][j] + " |"
		print(row)
		print("|___|___|___|___|___|___|___|___|")
def get_piece(x, y):
	
	return board[y][x]
def get_legal_moves(x, y):
	current_legal_moves = []

	#White
	if  (get_piece(x, y) == "R"):	#Rook	
		ix = 0
		iy = 0
		while(True): #Right
			iy += 1
			if  (check_for_black_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_white_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Left
			iy -= 1
			if  (check_for_black_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_white_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up
			ix += 1
			if  (check_for_black_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_white_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down
			ix -= 1
			if  (check_for_black_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_white_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
	elif(get_piece(x, y) == "N"):	#Knight	
		try:
			if(check_for_black_pieces_or_none(x+1, y+2)):	#Top
				current_legal_moves.append([x+1, y+2])
			if(check_for_black_pieces_or_none(x-1, y+2)):
				current_legal_moves.append([x-1, y+2])
		except:
			pass
		try:
			if(check_for_black_pieces_or_none(x+2, y+1)):	#Right
				current_legal_moves.append([x+2, y+1])
			if(check_for_black_pieces_or_none(x+2, y-1)):
				current_legal_moves.append([x+2, y-1])
		except:
			pass
		try:
			if(check_for_black_pieces_or_none(x+1, y-2)):	#Bottom
				current_legal_moves.append([x+1, y-2])
			if(check_for_black_pieces_or_none(x-1, y-2)):
				current_legal_moves.append([x-1, y-2])
		except:
			pass
		try:
			if(check_for_black_pieces_or_none(x-2, y+1)):	#left
				current_legal_moves.append([x-2, y+1])
			if(check_for_black_pieces_or_none(x-2, y-1)):
				current_legal_moves.append([x-2, y-1])
		except:
			pass
	elif(get_piece(x, y) == "B"):	#Bishop	
		ix = 0
		iy = 0
		while(True): #Up/right
			ix += 1
			iy += 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/right
			ix -= 1
			iy += 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/left
			ix -= 1
			iy -= 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up/left
			ix += 1
			iy -= 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break#
	elif(get_piece(x, y) == "Q"):	#Queen	
		#Horisontal/vertikal
		ix = 0
		iy = 0
		while(True): #Right
			iy += 1
			if  (check_for_black_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_white_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Left
			iy -= 1
			if  (check_for_black_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_white_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up
			ix += 1
			if  (check_for_black_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_white_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down
			ix -= 1
			if  (check_for_black_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_white_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break

		#Vertical
		ix = 0
		iy = 0
		while(True): #Up/right
			ix += 1
			iy += 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/right
			ix -= 1
			iy += 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/left
			ix -= 1
			iy -= 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up/left
			ix += 1
			iy -= 1
			if  (check_for_black_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_white_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
	elif(get_piece(x, y) == "K"):	#King 	
		if(check_for_black_pieces_or_none(x+1, y)):
			current_legal_moves.append([x+1, y])
		if(check_for_black_pieces_or_none(x+1, y+1)):
			current_legal_moves.append([x+1, y+1])
		if(check_for_black_pieces_or_none(x, y+1)):
			current_legal_moves.append([x, y+1])
		if(check_for_black_pieces_or_none(x-1, y+1)):
			current_legal_moves.append([x-1, y+1])
		if(check_for_black_pieces_or_none(x-1, y)):
			current_legal_moves.append([x-1, y])
		if(check_for_black_pieces_or_none(x-1, y-1)):
			current_legal_moves.append([x-1, y-1])
		if(check_for_black_pieces_or_none(x, y-1)):
			current_legal_moves.append([x, y-1])
		if(check_for_black_pieces_or_none(x+1, y-1)):
			current_legal_moves.append([x+1, y-1])
	elif(get_piece(x, y) == "P"):	#Pawn	
		if(get_piece(x, y+1) == None):
			current_legal_moves.append([x, y+1])
			if(get_piece(x, y+2) == None) and (y == 2):
				current_legal_moves.append([x, y+2])
		if(check_for_black_pieces(x-1, y+1)):
			current_legal_moves.append([x-1, y+1])
		if(check_for_black_pieces(x+1, y+1)):
			current_legal_moves.append([x+1, y+1])

	
	#Black
	elif(get_piece(x, y) == "r"):	#Rook	
		ix = 0
		iy = 0
		while(True): #Right
			iy += 1
			if  (check_for_white_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_black_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Left
			iy -= 1
			if  (check_for_white_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_black_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up
			ix += 1
			if  (check_for_white_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_black_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down
			ix -= 1
			if  (check_for_white_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_black_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
	elif(get_piece(x, y) == "n"):	#Knight	
		try:
			if(check_for_white_pieces_or_none(x+1, y+2)):	#Top
				current_legal_moves.append([x+1, y+2])
			if(check_for_white_pieces_or_none(x-1, y+2)):
				current_legal_moves.append([x-1, y+2])
		except:
			pass
		try:
			if(check_for_white_pieces_or_none(x+2, y+1)):	#Right
				current_legal_moves.append([x+2, y+1])
			if(check_for_white_pieces_or_none(x+2, y-1)):
				current_legal_moves.append([x+2, y-1])
		except:
			pass
		try:
			if(check_for_white_pieces_or_none(x+1, y-2)):	#Bottom
				current_legal_moves.append([x+1, y-2])
			if(check_for_white_pieces_or_none(x-1, y-2)):
				current_legal_moves.append([x-1, y-2])
		except:
			pass
		try:
			if(check_for_white_pieces_or_none(x-2, y+1)):	#left
				current_legal_moves.append([x-2, y+1])
			if(check_for_white_pieces_or_none(x-2, y-1)):
				current_legal_moves.append([x-2, y-1])
		except:
			pass
	elif(get_piece(x, y) == "b"):	#Bishop	
		ix = 0
		iy = 0
		while(True): #Up/right
			ix += 1
			iy += 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/right
			ix -= 1
			iy += 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/left
			ix -= 1
			iy -= 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up/left
			ix += 1
			iy -= 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
	elif(get_piece(x, y) == "q"):	#Queen	
		#Horisontal/vertikal
		ix = 0
		iy = 0
		while(True): #Right
			iy += 1
			if  (check_for_white_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_black_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Left
			iy -= 1
			if  (check_for_white_pieces(x, y+iy)):
				current_legal_moves.append([x, y+iy])
				break
			elif(check_for_black_pieces(x, y+iy)):
				break
			elif(get_piece(x, y+iy) == None):
				current_legal_moves.append([x, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up
			ix += 1
			if  (check_for_white_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_black_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down
			ix -= 1
			if  (check_for_white_pieces(x+ix, y)):
				current_legal_moves.append([x+ix, y])
				break
			elif(check_for_black_pieces(x+ix, y)):
				break
			elif(get_piece(x+ix, y) == None):
				current_legal_moves.append([x+ix, y])
			else:
				break

		#Vertical
		ix = 0
		iy = 0
		while(True): #Up/right
			ix += 1
			iy += 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/right
			ix -= 1
			iy += 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Down/left
			ix -= 1
			iy -= 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
		ix = 0
		iy = 0
		while(True): #Up/left
			ix += 1
			iy -= 1
			if  (check_for_white_pieces(x+ix, y+iy)):
				current_legal_moves.append([x+ix, y+iy])
				break
			elif(check_for_black_pieces(x+ix, y+iy)):
				break
			elif(get_piece(x+ix, y+iy) == None):
				current_legal_moves.append([x+ix, y+iy])
			else:
				break
	elif(get_piece(x, y) == "k"):	#King 	
		if(check_for_white_pieces_or_none(x+1, y)):
			current_legal_moves.append([x+1, y])
		if(check_for_white_pieces_or_none(x+1, y+1)):
			current_legal_moves.append([x+1, y+1])
		if(check_for_white_pieces_or_none(x, y+1)):
			current_legal_moves.append([x, y+1])
		if(check_for_white_pieces_or_none(x-1, y+1)):
			current_legal_moves.append([x-1, y+1])
		if(check_for_white_pieces_or_none(x-1, y)):
			current_legal_moves.append([x-1, y])
		if(check_for_white_pieces_or_none(x-1, y-1)):
			current_legal_moves.append([x-1, y-1])
		if(check_for_white_pieces_or_none(x, y-1)):
			current_legal_moves.append([x, y-1])
		if(check_for_white_pieces_or_none(x+1, y-1)):
			current_legal_moves.append([x+1, y-1])
	elif(get_piece(x, y) == "p"):	#Pawn	
		if(get_piece(x, y-1) == None):
			current_legal_moves.append([x, y-1])
			if(get_piece(x, y-2) == None) and (y == 7):
				current_legal_moves.append([x, y-2])
		if(check_for_white_pieces(x-1, y-1)):
			current_legal_moves.append([x-1, y-1])
		if(check_for_white_pieces(x+1, y-1)):
			current_legal_moves.append([x+1, y-1])

	return current_legal_moves
def check_for_white_pieces_or_none(x, y):
	for i in white_pieces:
		if((get_piece(x, y) == i) or (get_piece(x, y) == None)):
			return True
	return False
def check_for_white_pieces(x, y):
	for i in white_pieces:
		if(get_piece(x, y) == i):
			return True
	return False
def check_for_black_pieces_or_none(x, y):
	for i in black_pieces:
		if((get_piece(x, y) == i) or (get_piece(x, y) == None)):
			return True
	return False
def check_for_black_pieces(x, y):
	for i in black_pieces:
		if(get_piece(x, y) == i):
			return True
	return False
def move(x1, y1, x2, y2):
	fro = get_piece(x1, y1)
	t   = get_piece(x2, y2)

	if([x2, y2] in get_legal_moves(x1, y1)):
		board[y2][x2] = get_piece(x1, y1)
		board[y1][x1] = None
def change():
	for i in range(1, 9):
		if(board[1][i] == "p"):
			while(True):
				a = input("Type in the piece you want to change the pawn into: ")
				if ((a in black_pieces) and (a != "p")):
					board[1][i] = a
					break
	for i in range(1, 9):
		if(board[8][i] == "P"):
			while(True):
				a = input("Type in the piece you want to change the pawn into: ")
				if ((a in white_pieces) and (a != "P")):
					board[8][i] = a
					break
def get_move(white):
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	while(True):
		in1 = list(input("Select piece to move. Format (x y). Example '1 1': "))
		try:
			x1 = int(in1[0])
			y1 = int(in1[2])
			if((len(get_legal_moves(x1, y1)) != 0) and ((white and get_piece(x1, y1) in white_pieces) or (not white and get_piece(x1, y1) in black_pieces))):
				print("Valid moves:", get_legal_moves(x1, y1))
				break
			print("You cannot move that")
		except:
			print("Not valid")
	while(True):
		in2 = list(input("Select where to move. Format (x y). Example '2 1': "))
		try:
			x2 = int(in2[0])
			y2 = int(in2[2])
			if([x2, y2] in get_legal_moves(x1, y1)):
				break
			print("Not valid move")
		except:
			print("Not valid")

	move(x1, y1, x2, y2)
	change()
def enPassant():
	k=1
def main():
	#make_board(board_string)
	global white
	while(True):
		present_board()
		if(white):
			print("White's turn!")
		elif(not white):
			print("Black's turn!")
		get_move(white)
		white = not white

make_board(board_string )
print(get_piece(1,2))
print(get_legal_moves(1,2))
for i in range(len(board)):
 	print(board[i])

main()


#LATER
#king hiding
#en passant