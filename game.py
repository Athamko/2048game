import random
import copy


class Game():

    def __init__(self, board_size: int = 4, starting_blocks: int = 2):

        assert board_size >= 2, f"Board too small!"
        assert starting_blocks <= board_size, f"Too many starting blocks!"

        self.board_size = board_size
        self.start_blocks = starting_blocks

        play = input("Ready to play?.... Type 'yes' to play  ")
        if play == "yes":
            print("Starting the game...")
            gameOver = False
            board = self.newBoard()
            print("Type _ to go _:\n'w' - up\n's' - down\n'a' - left\n'd' - right\nor 'exit' to end the game.")

            while not gameOver:
                self.display(board)
                tmpBoard = copy.deepcopy(board)
                move = input("Whats your next move?  ")
                if move == "w":
                    board = self.moveUp(board)
                elif move == "s":
                    board = self.moveDown(board)
                elif move == "a":
                    board = self.moveLeft(board)
                elif move == "d":
                    board = self.moveRight(board)
                elif move == "exit":
                    gameOver = True
                    continue
                else:
                    print("Invalid input. Try again!")
                    continue
                if board == tmpBoard:
                    print("Try a different move!")
                    continue

                board = self.addNumber(board)

                if self.win(board):
                    print("--------------------")
                    self.display(board)
                    print("CONGRATS, YOU WON!")
                    gameOver = True
                if self.loss(board = board):
                    print("--------------------")
                    self.display(board)
                    gameOver = True
                    print("You lost! GAME OVER")



    
    def display(self,board):
        largest = 1
        for row in range(self.board_size):
            if len(str(max(board[row]))) > largest:
                largest = len(str(max(board[row])))

        for i in range(self.board_size):
            currRow = "|"
            for y in range(self.board_size):
                currRow += " "*(largest - len(str(board[i][y]))) + str(board[i][y]) + "|"
            print(currRow)

    def moveOneRowLeft(self,row):
        for _ in range(self.board_size-1):
            for i in range(self.board_size-1,-0,-1):
                if row[i-1] == 0:
                    row[i-1] = row[i]
                    row[i] = 0


        for i in range(self.board_size-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0

        for i in range(self.board_size-1,0,-1):
                if row[i-1] == 0:
                    row[i-1] = row[i]
                    row[i] = 0

        return row
    
    #we write this function so we dont have to write different functions for moving left and right
    def reverse(self,board):
        new = [row[::-1] for row in board]
        return new

            


    #we write this function so we dont have to write different functions for moving up and down
    def transpose(self,board):
        for x in range(self.board_size):
            for y in range(x,self.board_size):
                if x != y:
                    currentNum = board[x][y]
                    board[x][y] = board[y][x]
                    board[y][x] = currentNum
        return board


#All the moves
    def moveLeft(self,board):
        for rowNum in range(self.board_size):
            board[rowNum] = self.moveOneRowLeft(board[rowNum])
        return board
    
    def moveRight(self,board):
        return self.reverse(self.moveLeft(self.reverse(board=board)))
    
    def moveUp(self,board):
        return self.transpose(self.moveLeft(self.transpose(board=board)))
    
    def moveDown(self,board):
        return self.transpose(self.moveRight(self.transpose(board=board)))
    
    #this add number after every move
    def addNumber(self,board):
        done = False
        while done == False:
            x,y = random.randint(0,self.board_size-1),random.randint(0,self.board_size-1)
            if board[x][y] == 0:
                done = True
                if random.randint(1,10) == 1:
                    board[x][y] = 4
                else:
                    board[x][y] = 2
        return board
    
    #a function that fully generates a new board according to your specifics
    def newBoard(self):
        board = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(0)
            board.append(row)

        numsToAdd = self.start_blocks

        while numsToAdd > 0:
            x,y = random.randint(0,self.board_size-1),random.randint(0,self.board_size-1)
            if board[x][y] == 0:
                numsToAdd -=1
                if random.randint(1,10) == 1:
                    board[x][y] = 4
                else:
                    board[x][y] = 2

        return board
    
    #these functions detect wheter you lost or won
    def win(self,board):
        for row in board:
            if 2048 in row:
                return True
            return False
    
    def loss(self,board):
        tmpB1 = copy.deepcopy(board)
        tmpB2 = copy.deepcopy(board)

        tmpB2 = self.moveDown(tmpB2)
        if tmpB1 == tmpB2:
            tmpB2 = self.moveUp(tmpB2)
            if tmpB1 == tmpB2:
                tmpB2 = self.moveLeft(tmpB2)
                if tmpB1 == tmpB2:
                    tmpB2 = self.moveRight(tmpB2)
                    if tmpB1 == tmpB2:
                        return True
        return False




twoThousandAndTwentyFour = Game()




