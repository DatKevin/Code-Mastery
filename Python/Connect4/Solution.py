class Connect4():

    def __init__(self):
        self.board = [
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','','']            
        ]
        
        self.playeroneturn = True
        self.gameover = False
    def play(self, col):
        if self.gameover:
            return("Game has finished!")
        if self.board[0][col]:
            return "Column full!"
        if self.playeroneturn:
            tile = "X"
        else:
            tile = "O"    
        for row in self.board[::-1]:
            if not row[col]:
                row[col] = tile
                break
        for row in self.board:
            for piece in range(0,4):
                win = True
                for pieceinarow in range (0,4):  
                    if tile != row[piece + pieceinarow]:
                        win = False
                        break
                if win:
                    self.gameover = True
                    if self.playeroneturn:
                        return("Player 1 wins!")
                    else:
                        return("Player 2 wins!")
        for column in range(0, 7):
            for row in range(0,3):
                win = True
                for rowafter in range(0,4):
                    if tile != self.board[row + rowafter][column]:
                        win = False
                        break
                if win:
                    self.gameover = True
                    if self.playeroneturn:
                        return("Player 1 wins!")
                    else:
                        return("Player 2 wins!")
        for column in range(0, 4):
            for row in range(0,3):
                win = True
                for diagonal in range(0,4):
                    if tile != self.board[row + diagonal][column + diagonal]:
                        win = False
                        break
                if win:
                    self.gameover = True
                    if self.playeroneturn:
                        return("Player 1 wins!")
                    else:
                        return("Player 2 wins!")
        for column in range(3, 7):
            for row in range(0, 3):
                win = True
                for diagonal in range(0,4):
                    if tile != self.board[row + diagonal][column - diagonal]:
                        win = False
                        break
                if win:
                    self.gameover = True
                    if self.playeroneturn:
                        return("Player 1 wins!")
                    else:
                        return("Player 2 wins!")
        if self.playeroneturn:
            self.playeroneturn = False
            print(self.board)
            return("Player 1 has a turn")
        else:
            print(self.board)
            self.playeroneturn = True
            return("Player 2 has a turn")