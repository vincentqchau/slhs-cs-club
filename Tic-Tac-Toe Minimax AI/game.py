#Tic-Tac-Toe game
class Game:

    def __init__(self):
        global board 
        global piece
        board = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        piece = True

    def get_board(self):
        return board
    
    def get_piece(self):
        return piece
    
    def reset(self):
        global piece
        global board
        board = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        piece = True

    def check_win(self):
        curr = 'X' if piece else 'O'
        for i in range(0, 3):
            if board[i][0] == curr and board[i][1] == curr and board[i][2] == curr:
                return True
            if board[0][i] == curr and board[1][i] == curr and board[2][i] == curr:
                return True
        if board[0][0] == curr and board[1][1] == curr and board[2][2] == curr:
            return True
        elif board[0][2] == curr and board[1][1] == curr and board[2][0] == curr:
            return True
        return False

    def switch_turn(self):
        global piece
        piece = not piece

    def set_piece(self, row, column):
        global board
        global piece
        board[int(row)][int(column)] = 'X' if piece else 'O'

