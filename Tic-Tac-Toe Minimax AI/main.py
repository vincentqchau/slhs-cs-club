from game import Game
from minimax import AI

game_ = Game()
ai = AI()

def print_state():
    for row in game_.get_board():
        for col in row:
            print(col if col != '0' else ' ', end="|")
        print('\n------')

def run():
    while True:
        print_state()
        print()
        if game_.get_piece():
            r, c = int(input()), int(input())
            game_.set_piece(r, c)
        else:
            coords = [-1, -1]
            board = game_.get_board()
            spaces = game_.get_spaces()-1
            maxEval = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '0':
                        board[i][j] = 'O'
                        evaluation = ai.minimax(board, spaces, False, float("-inf"), float("inf"))
                        if evaluation > maxEval:
                            coords = [i, j]
                            maxEval = evaluation
                        board[i][j] = '0'
            game_.set_piece(coords[0], coords[1])
        win, piece = game_.check_win()
        if win:
            print(piece, 'wins')
            break
        elif game_.get_spaces() == 0:
            print('Tie')
            break
        game_.switch_turn()
    print_state()

run()