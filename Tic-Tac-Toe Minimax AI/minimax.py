import copy

class AI:

    def check_win(self, board):
        for i in range(3):
            if board[i][0] != '0' and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            if board[0][i] != '0' and board[0][i] == board[1][i] ==  board[2][i]:
                return board[0][i]
        if board[0][0] != '0' and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] != '0' and board[2][0] == board[1][1] == board[0][2]:
            return board[0][2]
        return '0'

    def static_evaluation(self, win, board):
        if win == 'O':
            return 100000 - board[0].count('0') - board[1].count('0') - board[2].count('0')
        elif win == 'X':
            return -100000 + board[0].count('0') + board[1].count('0') + board[2].count('0')
        return 50000

    def minimax(self, board, depth, isMaximizing, alpha, beta):
        win = self.check_win(board)
        if depth == 0 or win != '0':
            return self.static_evaluation(win, board)
        if isMaximizing:
            maxEvaluation = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '0':
                        temp = copy.deepcopy(board)
                        temp[i][j] = 'O'
                        eval = self.minimax(temp, depth-1, False, alpha, beta)
                        maxEvaluation = max(maxEvaluation, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            return maxEvaluation
            return maxEvaluation
        else:
            minEvaluation = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '0':
                        temp = copy.deepcopy(board)
                        temp[i][j] = 'X'
                        eval = self.minimax(temp, depth-1, True, alpha, beta)
                        minEvaluation = min(minEvaluation, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            return minEvaluation
            return minEvaluation

