import copy

class GameState:

## Initialize all required variables
boxes = [(s,t) for s in [0,1,2] for t in [0,1]]
boardDict = {}
player1Start=False
player2Start=False
p1Move=False
p2Move=False
p1Box=()
p2Box=()

def __init__(self):
	## Set the Active player TRUE & initialize the board as Dictionary with keys for
	## boxes and value 0 or 1 if it is visited or not.
	self.p1Move = True
	for box in self.boxes: self.boardDict[box] = 0
	self.boardDict[(2,1)]=1

def forecast_move(self, move):
	""" Return a new board object with the specified move
	applied to the current game state.
	Parameters
	----------
	move: tuple
	The target position for the active player's next move
	"""
	## Copy the exsiting gamestate to new gamestate and change the player.
	newBoard = copy.deepcopy(self)

	if newBoard.p1Move==True:
		newBoard.p1Box=move
		newBoard.p1Move=False
		newBoard.p2Move=True
	else:
		newBoard.p2Box=move
		newBoard.p2Move=False
		newBoard.p1Move=True
			
	newBoard.boardDict[move]=1
	return(newBoard)

def get_legal_moves(self):
	""" Return a list of all legal moves available to the
	active player.  Each player should get a list of all
	empty spaces on the board on their first move, and
	otherwise they should get a list of all open spaces
	in a straight line along any row, column or diagonal
	from their current position. (Players CANNOT move
	through obstacles or blocked squares.) Moves should
	be a pair of integers in (column, row) order specifying
	the zero-indexed coordinates on the board.
	"""
	
	## Return empty boxes if game has just started else use the rules ( row, column or diagonal ) to identify the 
	## legal moves for a player
	if self.player1Start==False:
		legalMoves = [box for box in self.boxes if self.boardDict[box] != 1]
		self.player1Start=True
		return legalMoves
	elif self.player2Start==False:
		legalMoves = [box for box in self.boxes if self.boardDict[box] != 1]
		self.player2Start=True
		return legalMoves
	else:
		currentMove=(0,0)
		rowWiseLegalMoves=[]
		for rowBoxIndex in range(currentMove[0]+1, 3):
			if self.boardDict[(rowBoxIndex, currentMove[1])] != 1:
				rowWiseLegalMoves.append((rowBoxIndex, currentMove[1]))
			else:
				break

		### Get col-wise legal moves
		colWiseLegalMoves = [] 
		for colBoxIndex in range(currentMove[1]+1, 2):
			if self.boardDict[(currentMove[0],colBoxIndex)] != 1:
				colWiseLegalMoves.append((currentMove[0],colBoxIndex))						
			else:
				break

		### Get diagnoal-wise legal moves
		diagonalLegalMoves = []
		for rowBoxIndex in range(currentMove[0]+1, 3):
			for colBoxIndex in range(currentMove[1]+1, 2):
				if self.boardDict[(rowBoxIndex, colBoxIndex)] != 1:
					diagonalLegalMoves.append((rowBoxIndex,colBoxIndex))
				else:
					break								

		legalMoves = rowWiseLegalMoves + colWiseLegalMoves + diagonalLegalMoves
		return legalMoves
